#!/usr/bin/env python3
''' Main file
'''

LFUCache = __import__('lfu').LFUCache


if __name__ == '__main__':
    lfu_cache = LFUCache(3)
    lfu_cache.put(1, 'A')
    lfu_cache.put(2, 'B')
    lfu_cache.put(3, 'C')
    getKey = lfu_cache.get(3)
    print(getKey)
    getKey = lfu_cache.get(3)
    print(getKey)
    getKey = lfu_cache.get(2)
    print(getKey)
    lfu_cache.put(4, 'D')  # Evicts key 1
    print(lfu_cache.cache)  # Output: {2: 'B', 3: 'C', 4: 'D'}
