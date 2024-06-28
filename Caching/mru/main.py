#!/usr/bin/env python3
''' Main file
'''

MRUCache = __import__('mru').MRUCache


if __name__ == '__main__':
    mru_cache = MRUCache(3)
    mru_cache.put(1, 'A')
    mru_cache.put(2, 'B')
    mru_cache.put(3, 'C')
    getKey = mru_cache.get(3)
    print(getKey)
    getKey = mru_cache.get(3)
    print(getKey)
    getKey = mru_cache.get(1)
    print(getKey)
    mru_cache.put(4, 'D')  # Evicts key 1
    print(mru_cache.cache)  # Output: {2: 'B', 3: 'C', 4: 'D'}
