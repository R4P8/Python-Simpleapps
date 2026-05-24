from app.repositories.product_repository import ProductRepository


class ProductService:

    @staticmethod
    def get_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product(product_id):
        return ProductRepository.get_product_by_id(product_id)