from app.database import get_connection
from app.models.product_model import Product


class ProductRepository:

    @staticmethod
    def get_all_products():
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT id, name, price FROM products"
        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        products = [
            Product(id=row[0], name=row[1], price=row[2]).to_dict()
            for row in rows
        ]

        return products

    @staticmethod
    def get_product_by_id(product_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT id, name, price FROM products WHERE id = %s"
        cursor.execute(query, (product_id,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if not row:
            return None

        product = Product(
            id=row[0],
            name=row[1],
            price=row[2]
        )

        return product.to_dict()