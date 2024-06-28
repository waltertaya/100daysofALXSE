#!/usr/bin/env python3
''' Implements fifo
'''


class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key):
        return self.cache.get(key, -1)

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                oldest = self.queue.pop(0)
                del self.cache[oldest]
            self.cache[key] = value
            self.queue.append(key)
