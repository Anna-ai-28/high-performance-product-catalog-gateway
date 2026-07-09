from app.cache.cache_service import CacheService
from app.providers.factory import ProviderFactory


class CatalogService:

    def __init__(self):

        self.provider = ProviderFactory.create()

        self.cache = CacheService()

    async def get_products(self):

        cache_key = "catalog:products"

        cached = await self.cache.get(cache_key)

        if cached is not None:
            return cached

        products = await self.provider.get_products()

        await self.cache.set(
            cache_key,
            products
        )

        return products