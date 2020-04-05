from flask_restx import Namespace

from services.hello.resources import HelloWorld

hello_namespace = Namespace('hello', description='Hello namespace')
hello_namespace.add_resource(HelloWorld, '/')
