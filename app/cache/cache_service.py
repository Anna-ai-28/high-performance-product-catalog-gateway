import json
import logging

from redis.exceptions import RedisError

from app.cache.redis_client import redis_client
from app.core.settings import CACHE_TTL


logger = logging.getLogger(__name__)


class CacheService:

    async def get(self, key: str):

        try:

            value = await redis_client.get(key)

            if value is None:
                return None

            return json.loads(value)

        except RedisError as exc:

            logger.exception(
                "Redis GET failed. Bypassing cache. %s",
                exc
            )

            return None

    async def set(self, key: str, value):

        try:

            serialized = json.dumps(value)

            await redis_client.set(
                key,
                serialized,
                ex=CACHE_TTL
            )

        except RedisError as exc:

            logger.exception(
                "Redis SET failed. Continuing without cache. %s",
                exc
            )