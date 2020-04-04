from flask import Flask

from services.hello import hello_world


def create_routing(app: Flask):
    app.add_url_rule('/', view_func=hello_world)


def create_app():
    app = Flask(__name__)
    create_routing(app)
    return app
