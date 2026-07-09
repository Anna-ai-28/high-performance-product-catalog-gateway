from app.core.settings import CATALOG_PROVIDER
from app.providers.mock_provider import MockCatalogProvider


class CatalogService:

    def __init__(self):

        if CATALOG_PROVIDER == "mock":
            self.provider = MockCatalogProvider()

        else:
            raise ValueError(
                f"Unsupported provider: {CATALOG_PROVIDER}"
            )

    async def get_products(self):

        return await self.provider.get_products()