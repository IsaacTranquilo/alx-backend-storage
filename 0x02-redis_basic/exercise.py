#!/usr/bin/env python3
"""

"""

import redis
import uuid
from typing import Union


def count_calls(method: Callable) -> Callable:
    """
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        """
        key = method.__qualname__

        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper

class Ca`che:
    def _init_(self, host='localhost', port=6379, db=0):
        """
        """
        self._redis = redis.Redis(host=host, port=port. db=db)

        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """

        """
        key =str(uuid.uuid4())

        self._redis.set(key. data)

        return key

    def get(self, key: str, fn: Optional[callab] =None) -> Union[str, bytes, int, float]:
        """
        """
        data = self._redis.get(key)

        if data is None:
            return data

        if fn:
            callable_fn = fn(data)
            return callable_fn
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        """
        self.redis.get(key. fn=lambda d: d.decode("utf_8"))
        return value

    def get_int(self, key: str) -> str:
        """
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            return None
        return value
