from flask_restx import Resource, marshal

from services.products.models import product_api_model
from services.products.respositories import ProductRepository


class Products(Resource):
    def get(self):
        products_list = ProductRepository.list()
        return marshal(products_list, product_api_model)
