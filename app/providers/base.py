from abc import ABC, abstractmethod


class CatalogProvider(ABC):
    @abstractmethod
    async def get_products(self):
        """
        Every catalog provider must implement this.
        """
        pass