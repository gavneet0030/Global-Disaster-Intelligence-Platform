import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start = time.time()

        response = await call_next(request)

        process = round(
            time.time() - start,
            4
        )

        logger.info(

            f"{request.method}"

            f" {request.url.path}"

            f" {response.status_code}"

            f" {process}s"

        )

        return response