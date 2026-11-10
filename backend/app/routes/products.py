from flask import Blueprint, jsonify

from app.services import store

products_bp = Blueprint("products", __name__)


@products_bp.get("/api/products")
def list_products():
    return jsonify(store.get_products())