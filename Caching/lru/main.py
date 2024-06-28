#!/usr/bin/env python3
''' Main file
'''

LRUCache = __import__('lru').LRUCache


if __name__ == '__main__':
    lru_cache = LRUCache(3)
    lru_cache.put(1, 'A')
    lru_cache.put(2, 'B')
    lru_cache.put(3, 'C')
    getKey = lru_cache.get(1)
    print(getKey)
    getKey = lru_cache.get(3)
    print(getKey)
    getKey = lru_cache.get(3)
    print(getKey)
    lru_cache.put(4, 'D')  # Evicts key 1
    print(lru_cache.cache)  # Output: {2: 'B', 3: 'C', 4: 'D'}
