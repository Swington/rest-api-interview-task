from typing import List

from services.products.models import ProductModel


class ProductsRepository:
    @classmethod
    def list(cls) -> List[ProductModel]:
        return []
