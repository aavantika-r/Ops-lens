from app.services.db import get_cursor

PRODUCT_COLUMNS = "id, name, category, price, emoji, description"


def get_products():
    with get_cursor() as cur:
        cur.execute(f"SELECT {PRODUCT_COLUMNS} FROM products ORDER BY id")
        return [dict(r) for r in cur.fetchall()]


def get_product(product_id):
    with get_cursor() as cur:
        cur.execute(f"SELECT {PRODUCT_COLUMNS} FROM products WHERE id = %s", (product_id,))
        row = cur.fetchone()
        return dict(row) if row else None


def save_order(order):
    c = order["customer"]
    # oru transaction: customer + order + items ellam serndhu save aagum, illana rollback
    with get_cursor() as cur:
        cur.execute(
            "INSERT INTO customers (name, phone, address) VALUES (%s, %s, %s) RETURNING id",
            (c["name"], c["phone"], c["address"]),
        )
        customer_id = cur.fetchone()["id"]

        cur.execute(
            "INSERT INTO orders (customer_id, total, status) VALUES (%s, %s, %s) RETURNING id",
            (customer_id, order["total"], order["status"]),
        )
        order_id = cur.fetchone()["id"]

        for item in order["items"]:
            cur.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) "
                "VALUES (%s, %s, %s, %s)",
                (order_id, item["product_id"], item["quantity"], item["price"]),
            )
    return get_order(order_id)


def get_order(order_id):
    with get_cursor() as cur:
        cur.execute(
            "SELECT o.id, o.total, o.status, o.created_at, c.name, c.phone, c.address "
            "FROM orders o JOIN customers c ON c.id = o.customer_id WHERE o.id = %s",
            (order_id,),
        )
        row = cur.fetchone()
        if row is None:
            return None

        cur.execute(
            "SELECT oi.product_id, p.name, oi.price, oi.quantity "
            "FROM order_items oi JOIN products p ON p.id = oi.product_id "
            "WHERE oi.order_id = %s ORDER BY oi.id",
            (order_id,),
        )
        items = [dict(r) for r in cur.fetchall()]

    return {
        "id": row["id"],
        "customer": {"name": row["name"], "phone": row["phone"], "address": row["address"]},
        "items": items,
        "total": row["total"],
        "status": row["status"],
        "created_at": row["created_at"].isoformat(),
    }