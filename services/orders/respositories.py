from typing import List, Dict, Any

from services.orders.models import OrderModel


class OrdersRepository:
    @classmethod
    def list(cls) -> List[OrderModel]:
        return []

    @classmethod
    def get(cls, order_uuid: str) -> OrderModel:
        return OrderModel(order_uuid, [])

    @classmethod
    def create(cls, data: Dict[str, Any]) -> OrderModel:
        return OrderModel(**data)

    @classmethod
    def update(cls, order_uuid: str, data: Dict[str, Any]) -> OrderModel:
        order = cls.get(order_uuid)
        order.update(data)
        return order
