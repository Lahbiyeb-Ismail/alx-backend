#!/usr/bin/env python3

"""
LRUCache class that inherits from BaseCaching and implements
a LRU (Least Recently Used) caching system.
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and implements
    a LRU (Least Recently Used) caching system.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance.
        """
        super().__init__()
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
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
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

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
