#!/usr/bin/env python3

"""
LIFOCache class that inherits from BaseCaching and implements
a LIFO (Last In First Out) caching system
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements
    a LIFO (Last In First Out) caching system.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance.
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

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

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
        if key is None:
            return None

        return self.cache_data.get(key)
