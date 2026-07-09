from app.core.settings import CATALOG_PROVIDER

from app.providers.mock_provider import MockCatalogProvider


class ProviderFactory:

    @staticmethod
    def create():

        providers = {
            "mock": MockCatalogProvider,
        }

        provider_class = providers.get(CATALOG_PROVIDER)

        if provider_class is None:
            raise ValueError(
                f"Unsupported catalog provider: {CATALOG_PROVIDER}"
            )

        return provider_class()