from typing import List

from services.products.models import Product


class ProductRepository:
    @classmethod
    def list(cls) -> List[Product]:
        return []
