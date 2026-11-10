import logging
from datetime import datetime, timezone

from app.services import store

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


def create_order(payload):
    customer = payload.get("customer") or {}
    items = payload.get("items") or []

    # Validate customer details
    for field in ("name", "phone", "address"):
        if not str(customer.get(field, "")).strip():
            raise ValidationError(f"customer.{field} is required")

    # Validate order items
    if not items:
        raise ValidationError("items cannot be empty")

    order_items = []
    total = 0

    for item in items:
        pid = item.get("product_id")
        product = store.get_product(pid) if isinstance(pid, int) else None

        qty = item.get("quantity")

        if product is None:
            raise ValidationError(
                f"product {item.get('product_id')} not found"
            )

        if not isinstance(qty, int) or qty < 1:
            raise ValidationError("quantity must be a positive integer")

        # Get price from server, never trust the client
        order_items.append({
            "product_id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": qty,
        })

        total += product["price"] * qty

    # Save order
    order = store.save_order({
        "customer": {
            k: str(customer[k]).strip()
            for k in ("name", "phone", "address")
        },
        "items": order_items,
        "total": total,
        "status": "Placed",
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    logger.info("order created", extra={"order_id": order["id"]})

    return order