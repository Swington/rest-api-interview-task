from flask import Flask
from flask_restx import Api, Namespace

from services.hello import HelloWorld


def initialize_app():
    app = Flask(__name__)
    api = Api(app, doc='/swagger/')
    default_namespace = Namespace('')
    default_namespace.add_resource(HelloWorld, '/hello')
    api.add_namespace(default_namespace, path='/')
    return app
