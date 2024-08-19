#!/usr/bin/env python3

"""
LFUCache class that inherits from BaseCaching and implements
a LFU (Least Frequently Used) caching system with
LRU as a tie-breaker
"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and implements
    a LFU (Least Frequently Used) caching system with LRU as a tie-breaker.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance.
        """
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the least frequently used key
            min_freq = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
            if len(lfu_keys) > 1:
                # If there's a tie, use LRU to break it
                lfu_key = next(k for k in self.order if k in lfu_keys)
            else:
                lfu_key = lfu_keys[0]

            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            self.order.remove(lfu_key)
            print(f"DISCARD: {lfu_key}")

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.order.append(key)

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored in the cache, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
