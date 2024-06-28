#!/usr/bin/env python3
''' Implements LFU replacement policy
'''

from collections import defaultdict


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(int)
        self.min_freq = 0
        self.freq_list = defaultdict(list)

    def _update_freq(self, key):
        freq = self.freq[key]
        self.freq[key] += 1
        self.freq_list[freq].remove(key)
        if not self.freq_list[freq]:
            del self.freq_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.freq_list[freq + 1].append(key)

    def get(self, key):
        if key in self.cache:
            self._update_freq(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self._update_freq(key)
        else:
            if len(self.cache) >= self.capacity:
                evict_key = self.freq_list[self.min_freq].pop(0)
                del self.cache[evict_key]
                del self.freq[evict_key]
            self.cache[key] = value
            self.freq[key] = 1
            self.min_freq = 1
            self.freq_list[1].append(key)
