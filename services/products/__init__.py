from flask_restx import Namespace

from services.products.resources import ProductsResource

products_namespace = Namespace(
    'products', description='Namespace for performing operations on products'
)
products_namespace.add_resource(ProductsResource, '/')
