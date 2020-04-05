from typing import Optional

from flask_restx import Resource, marshal

from services.orders.models import order_api_model
from services.orders.respositories import OrdersRepository


class OrdersResource(Resource):
    def get(self, order_uuid: Optional[str] = None):
        if order_uuid is None:
            return marshal(OrdersRepository.list(), order_api_model)
