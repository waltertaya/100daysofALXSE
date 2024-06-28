#!/usr/bin/env python3
''' Implements LIFO as Cache Replacement policy
'''

from typing import Any


class LIFOCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.stack = []
    
    def get(self, key: int) -> Any:
        return self.cache.get(key, -1)
    
    def put(self, key: int, value: Any) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.stack) == self.capacity:
                newest = self.stack.pop(-1)
                del self.cache[newest]
            self.cache[key] = value
            self.stack.append(key)
