from flask import Flask
from flask_restx import Api

from services.hello import hello_namespace
from services.orders import orders_namespace
from services.products import products_namespace


def initialize_app():
    app = Flask(__name__)
    api = Api(app, doc='/swagger/')
    api.add_namespace(hello_namespace)
    api.add_namespace(products_namespace)
    api.add_namespace(orders_namespace)
    return app
