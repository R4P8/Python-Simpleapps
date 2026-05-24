from flask import jsonify
from app.services.product_service import ProductService


class ProductController:

    @staticmethod
    def get_all_products():
        products = ProductService.get_products()

        return jsonify({
            "success": True,
            "data": products
        }), 200

    @staticmethod
    def get_product_by_id(product_id):
        product = ProductService.get_product(product_id)

        if not product:
            return jsonify({
                "success": False,
                "message": "Product not found"
            }), 404

        return jsonify({
            "success": True,
            "data": product
        }), 200