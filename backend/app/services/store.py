# TEMPORARY in-memory store. Phase 4 la PostgreSQL ku replace pannuvom.
PRODUCTS = [
    {"id": 1, "name": "Margherita Pizza", "category": "Pizza", "price": 249, "emoji": "🍕", "description": "Classic cheese and tomato"},
    {"id": 2, "name": "Veg Burger", "category": "Burgers", "price": 149, "emoji": "🍔", "description": "Crispy patty with fresh veggies"},
    {"id": 3, "name": "Chicken Biryani", "category": "Rice", "price": 229, "emoji": "🍛", "description": "Aromatic basmati with spices"},
    {"id": 4, "name": "French Fries", "category": "Snacks", "price": 99, "emoji": "🍟", "description": "Golden and crunchy"},
    {"id": 5, "name": "Paneer Wrap", "category": "Wraps", "price": 139, "emoji": "🌯", "description": "Spiced paneer in soft roti"},
    {"id": 6, "name": "Cold Coffee", "category": "Drinks", "price": 119, "emoji": "🥤", "description": "Chilled and creamy"},
]

ORDERS = {}
_next_order_id = 1


def get_products():
    return PRODUCTS


def get_product(product_id):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)


def save_order(order):
    global _next_order_id
    order["id"] = _next_order_id
    _next_order_id += 1
    ORDERS[order["id"]] = order
    return order


def get_order(order_id):
    return ORDERS.get(order_id)