#!/usr/bin/env python3

"""
BasicCache class that inherits from BaseCaching and implements
a basic caching system with put and get methods
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and implements
    a basic caching system with put and get methods.
    """

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

        self.cache_data[key] = item

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
