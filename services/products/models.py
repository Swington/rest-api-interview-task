from flask_restx import fields

from services.products.namespaces import products_namespace

product_api_model = products_namespace.model(
    'product', {'uuid': fields.String, 'name': fields.String,}
)


class ProductModel:
    def __init__(self, uuid: str, name: str):
        self.uuid = uuid
        self.name = name
