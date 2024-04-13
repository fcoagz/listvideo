from typing import Any
from cachetools import TTLCache, TLRUCache

class Cache:
    def __init__(self, limit: bool, maxsize: float, timeout: float = None) -> None:
        try:     
            if limit is not True:
                self.cache = TLRUCache(maxsize=maxsize)
            else:
                self.cache = TTLCache(maxsize=maxsize, ttl=timeout)
        except Exception as e:
            raise e
        
    def get_data(self, key: str):
        if key not in self.cache:
            return None
        return self.cache[key]

    def set_data(self, key: str, value: Any):
        self.cache[key] = value