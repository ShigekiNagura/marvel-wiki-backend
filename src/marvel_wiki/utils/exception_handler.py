import typing as t
from contextlib import contextmanager

from loguru import logger
from rest_framework.exceptions import APIException
from rest_framework.views import Response, exception_handler


def custom_exception_handler(exc: Exception, context: dict) -> Response:
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    response = exception_handler(exc, context)
    return response


@contextmanager
def handle_except():
    try:
        yield
    except APIException as ex:
        logger.exception(ex)
        raise ex
    except Exception as ex:
        logger.exception(ex)
        raise APIException()