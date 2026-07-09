from fastapi import APIRouter

from app.services.catalog_service import CatalogService

router = APIRouter(
    prefix="/catalog",
    tags=["Catalog"]
)

catalog_service = CatalogService()


@router.get("/products")
async def get_products():
    return await catalog_service.get_products()
