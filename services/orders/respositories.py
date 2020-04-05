from typing import List

from services.orders.models import OrderModel


class OrdersRepository:
    @classmethod
    def list(cls) -> List[OrderModel]:
        return []

    @classmethod
    def get(cls, order_uuid: str) -> OrderModel:
        return OrderModel()
