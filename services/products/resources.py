from flask_restx import Resource

from services.products.namespaces import products_namespace
from services.products.models import product_api_model
from services.products.respositories import ProductsRepository


@products_namespace.route('/')
class ProductsResource(Resource):
    @products_namespace.marshal_list_with(product_api_model)
    def get(self):
        return ProductsRepository.list(), 200
