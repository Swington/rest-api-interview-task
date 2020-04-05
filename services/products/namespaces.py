from flask_restx import Namespace

products_namespace = Namespace(
    'products', description='Namespace for performing operations on products'
)
