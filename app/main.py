from fastapi import FastAPI

from app.api.catalog import router as catalog_router

app = FastAPI(
    title="High Performance Product Catalog Gateway",
    description="Scalable API Gateway",
    version="1.0.0"
)


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "catalog-gateway"
    }


app.include_router(catalog_router)