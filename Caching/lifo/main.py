#!/usr/bin/env python3
''' Main file
'''

LIFOCache = __import__('lifo').LIFOCache


if __name__ == '__main__':
    lifo_cache = LIFOCache(3)
    lifo_cache.put(1, 'A')
    lifo_cache.put(2, 'B')
    lifo_cache.put(3, 'C')
    lifo_cache.put(4, 'D')  # Evicts key 1
    getKey = lifo_cache.get(2)
    print(getKey)
    print(lifo_cache.cache)  # Output: {2: 'B', 3: 'C', 4: 'D'}
