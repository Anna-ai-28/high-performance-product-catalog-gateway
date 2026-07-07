from typing import List


class CatalogService:
    async def get_products(self) -> List[dict]:
        """
        Temporary mock implementation.

        Later this method will:
        1. Check Redis
        2. Fetch from external API on cache miss
        3. Update cache
        """

        return [
            {
                "id": 1,
                "name": "Laptop",
                "price": 75000
            },
            {
                "id": 2,
                "name": "Keyboard",
                "price": 2500
            },
            {
                "id": 3,
                "name": "Mouse",
                "price": 1200
            }
        ]