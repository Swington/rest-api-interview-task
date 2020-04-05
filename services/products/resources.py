from flask_restx import Resource, marshal

from services.products.models import product_api_model
from services.products.respositories import ProductsRepository


class ProductsResource(Resource):
    def get(self):
        products_list = ProductsRepository.list()
        return marshal(products_list, product_api_model)
