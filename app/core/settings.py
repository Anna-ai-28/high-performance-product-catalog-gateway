import os
from dotenv import load_dotenv

load_dotenv()

CATALOG_PROVIDER = os.getenv("CATALOG_PROVIDER", "mock")
CATALOG_API_URL = os.getenv("CATALOG_API_URL", "")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

CACHE_TTL = int(os.getenv("CACHE_TTL", "60"))