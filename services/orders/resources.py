from flask_restx import Resource, marshal

from services.orders.models import order_api_model
from services.orders.respositories import OrdersRepository


class OrdersListResource(Resource):
    def get(self):
        return marshal(OrdersRepository.list(), order_api_model)


class OrdersResource(Resource):
    def get(self, order_uuid: str):
        return marshal(OrdersRepository.get(order_uuid), order_api_model)
