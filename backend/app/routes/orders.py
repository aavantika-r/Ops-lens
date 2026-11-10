from flask import Blueprint, jsonify, request

from app.services import store
from app.services.order_service import ValidationError, create_order

orders_bp = Blueprint("orders", __name__)


@orders_bp.post("/api/orders")
def post_order():
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"error": "JSON body required"}), 400
    try:
        order = create_order(payload)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(order), 201


@orders_bp.get("/api/orders/<int:order_id>")
def get_order(order_id):
    order = store.get_order(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order)