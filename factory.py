from flask import Flask
from flask_restx import Api

from services.hello import hello_namespace


def initialize_app():
    app = Flask(__name__)
    api = Api(app, doc='/swagger/')
    api.add_namespace(hello_namespace)
    return app
