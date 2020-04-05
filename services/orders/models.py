from typing import List

from flask_restx import fields

from services.orders.namespaces import orders_namespace
from services.products.models import ProductModel, product_api_model

order_api_model = orders_namespace.model(
    'order', {'uuid': fields.String, 'products': fields.List(fields.Nested(product_api_model))}
)


class OrderModel:
    def __init__(self, uuid: str, products: List[ProductModel]):
        self.uuid = uuid
        self.products = products
