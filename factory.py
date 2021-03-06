from flask import Flask
from flask_restx import Api

from services.orders import orders_namespace
from services.products import products_namespace


def get_api(app: Flask) -> Api:
    return Api(app, version='1.0.0', title='Interview task REST API', doc='/swagger/')


def initialize_app():
    app = Flask(__name__)
    api = Api(app, doc='/swagger/')
    api.add_namespace(products_namespace)
    api.add_namespace(orders_namespace)
    return app
