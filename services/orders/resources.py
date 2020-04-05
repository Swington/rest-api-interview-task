from flask_restx import Resource

from services.orders.exceptions import OrderNotFound
from services.orders.models import order_api_model
from services.orders.namespaces import orders_namespace
from services.orders.respositories import OrdersRepository


@orders_namespace.route('/')
class OrdersListResource(Resource):
    @orders_namespace.marshal_list_with(order_api_model)
    def get(self):
        return OrdersRepository.list(), 200

    @orders_namespace.marshal_with(order_api_model)
    @orders_namespace.expect(order_api_model)
    def post(self):
        return OrdersRepository.create(self.api.payload), 201


@orders_namespace.route('/<string:order_uuid>')
class OrdersResource(Resource):
    def get(self, order_uuid: str):
        try:
            return (
                orders_namespace.marshal(OrdersRepository.get(order_uuid), order_api_model),
                200,
            )
        except OrderNotFound:
            return {}, 404

    @orders_namespace.expect(order_api_model)
    def put(self, order_uuid: str):
        try:
            return (
                orders_namespace.marshal(
                    OrdersRepository.update(order_uuid, self.api.payload), order_api_model
                ),
                200,
            )
        except OrderNotFound:
            return {}, 404

    def delete(self, order_uuid: str):
        try:
            return (
                orders_namespace.marshal(OrdersRepository.delete(order_uuid), order_api_model),
                200,
            )
        except OrderNotFound:
            return {}, 404
