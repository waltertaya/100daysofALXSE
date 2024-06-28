#!/usr/bin/env python3
''' Class implementation of the LRU Cache Replacement Policy
'''
from typing import Any


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    def get(self, key: int) -> Any:
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]
    
    def put(self, key: int, value: Any) -> None:
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
            self.cache[key] = value
        else:
            if len(self.order) == self.capacity:
                leastAccessed = self.order.pop(0)
                del self.cache[leastAccessed]
            
            self.cache[key] = value
            self.order.append(key)
