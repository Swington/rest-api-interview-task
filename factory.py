from flask import Flask
from flask_restful import Api

from services.hello import HelloWorld


def create_routing(api: Api):
    api.add_resource(HelloWorld, '/')


def create_app():
    app = Flask(__name__)
    api = Api(app)
    create_routing(api)
    return app
