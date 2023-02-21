#!/usr/bin/env python3
'''caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''FIFO Cache class
    '''
    active = []
    rm_item = 0

    def __init__(self) -> None:
        '''Init constructor method
        '''
        super().__init__()

    def put(self, key, item):
        '''Adds item to cache_data with provided key
        '''
        if key is None or item is None:
            return
        LRUCache.rm_item = 0
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            while list(self.cache_data.keys())[LRUCache.rm_item] in LRUCache.active:
                LRUCache.rm_item += 1
            if len(LRUCache.active) > 0:
                LRUCache.active.pop(0)
            rm_key = list(self.cache_data.keys())[LRUCache.rm_item]
            print("DISCARD: {}".format(rm_key))
            del self.cache_data[rm_key]

    def get(self, key):
        '''retrives item from cache_data with provided key
        '''
        LRUCache.active.append(key)
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
