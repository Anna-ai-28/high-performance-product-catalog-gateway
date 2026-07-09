from redis.asyncio import Redis

from app.core.settings import REDIS_HOST, REDIS_PORT

redis_client = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)