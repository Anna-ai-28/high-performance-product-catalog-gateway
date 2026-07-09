import os
from dotenv import load_dotenv

load_dotenv()

CATALOG_PROVIDER = os.getenv("CATALOG_PROVIDER", "mock")
CATALOG_API_URL = os.getenv("CATALOG_API_URL", "")