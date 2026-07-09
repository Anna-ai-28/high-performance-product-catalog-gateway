from fastapi import FastAPI
from app.api.catalog import router as catalog_router
from app.core.logging_config import configure_logging
from app.middleware.request_logging import request_logging_middleware
from app.core.exception_handlers import (
    unhandled_exception_handler,
)

configure_logging()

app = FastAPI(
    title="High Performance Product Catalog Gateway",
    description="Scalable API Gateway",
    version="1.0.0"
)

app.middleware("http")(request_logging_middleware)
app.add_exception_handler(
    Exception,
    unhandled_exception_handler,
)

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "catalog-gateway"
    }


app.include_router(catalog_router)
