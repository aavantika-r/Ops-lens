import logging

from flask import Blueprint, jsonify

from app.services.db import get_cursor

health_bp = Blueprint("health", __name__)
logger = logging.getLogger(__name__)


@health_bp.get("/health")
def health():
    try:
        with get_cursor() as cur:
            cur.execute("SELECT 1")
        return jsonify({"status": "ok", "database": "up"})
    except Exception:
        logger.exception("health check failed")
        return jsonify({"status": "unhealthy", "database": "down"}), 503