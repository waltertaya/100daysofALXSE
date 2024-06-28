#!/usr/bin/env python3
''' Main file
'''

FIFOCache = __import__('fifo').FIFOCache


if __name__ == '__main__':
    fifo_cache = FIFOCache(3)
    fifo_cache.put(1, 'A')
    fifo_cache.put(2, 'B')
    fifo_cache.put(3, 'C')
    fifo_cache.put(4, 'D')  # Evicts key 1
    getKey = fifo_cache.get(2)
    print(getKey)
    print(fifo_cache.cache)  # Output: {2: 'B', 3: 'C', 4: 'D'}
