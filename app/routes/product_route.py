from flask import Blueprint
from app.controllers.product_controller import ProductController

product_bp = Blueprint("product_bp", __name__)


product_bp.route("/products", methods=["GET"])(
    ProductController.get_all_products
)

product_bp.route("/products/<int:product_id>", methods=["GET"])(
    ProductController.get_product_by_id
)