from app.providers.factory import ProviderFactory


class CatalogService:

    def __init__(self):

        self.provider = ProviderFactory.create()

    async def get_products(self):

        return await self.provider.get_products()