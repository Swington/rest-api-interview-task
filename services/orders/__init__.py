from flask_restx import Namespace

from services.orders.resources import OrdersResource

orders_namespace = Namespace('orders', description='Namespace for performing operations on orders')

orders_namespace.add_resource(OrdersResource, '/')
