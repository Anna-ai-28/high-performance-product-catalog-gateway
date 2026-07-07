from fastapi import FastAPI

app = FastAPI(
    title="High Performance Product Catalog Gateway",
    description="A scalable API Gateway with Redis caching.",
    version="1.0.0"
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "catalog-gateway"
    }