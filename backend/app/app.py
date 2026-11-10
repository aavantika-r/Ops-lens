import logging
import time

from flask import Flask, g, request
from flask_cors import CORS

from app.logging_config import setup_logging
from app.routes.health import health_bp
from app.routes.orders import orders_bp
from app.routes.products import products_bp

logger = logging.getLogger("opslens.http")


def create_app():
    setup_logging()
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)

    @app.before_request
    def start_timer():
        g.start = time.perf_counter()

    @app.after_request
    def log_request(response):
        duration = (time.perf_counter() - g.start) * 1000
        logger.info(
            "request completed",
            extra={
                "method": request.method,
                "path": request.path,
                "status": response.status_code,
                "duration_ms": round(duration, 2),
            },
        )
        return response

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)