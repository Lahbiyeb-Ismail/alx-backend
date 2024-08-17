#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Any, Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            data = self.dataset()
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a hypermedia index from the dataset.

        Args:
          index (int, optional): The index of the dataset
          to retrieve. Defaults to None.
          page_size (int, optional): The number of items
          to include in each page. Defaults to 10.

        Returns:
          Dict[str, Any]: A dictionary containing the following information:
            - "index": The index of the retrieved dataset.
            - "next_index": The index of the next dataset, if available.
            - "page_size": The number of items in the retrieved dataset.
            - "data": The retrieved dataset.
        """
        assert index is not None and 0 <= index < len(self.dataset())
        indexed_dataset = self.indexed_dataset()

        data = []
        cur_index = index
        while len(data) < page_size and cur_index < len(self.dataset()):
            if cur_index in indexed_dataset:
                data.append(indexed_dataset[cur_index])
            cur_index += 1

        next_index = cur_index if cur_index < len(self.dataset()) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
