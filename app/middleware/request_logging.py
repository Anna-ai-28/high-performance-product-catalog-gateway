import logging
import time
import uuid

from fastapi import Request

logger = logging.getLogger(__name__)


async def request_logging_middleware(request: Request, call_next):

    request_id = str(uuid.uuid4())

    start = time.perf_counter()

    try:

        response = await call_next(request)

    except Exception:

        elapsed = (time.perf_counter() - start) * 1000

        logger.exception(
            "[%s] %s %s -> FAILED (%.2f ms)",
            request_id,
            request.method,
            request.url.path,
            elapsed,
        )

        raise

    elapsed = (time.perf_counter() - start) * 1000

    logger.info(
        "[%s] %s %s -> %s (%.2f ms)",
        request_id,
        request.method,
        request.url.path,
        response.status_code,
        elapsed,
    )

    response.headers["X-Request-ID"] = request_id

    return response