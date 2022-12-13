from functools import wraps
from decouple import config

from flask import request


def valid_auth(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        if 'x-api-key' not in request.headers:
            return "Credentials not present in request", 401
        elif request.headers['x-api-key'] not in config("X_API_KEY"):
            return "Credentials not valid", 401
        else:
            return func(*args, **kwargs)

    return func_wrapper
