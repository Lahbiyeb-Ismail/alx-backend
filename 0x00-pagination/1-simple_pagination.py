#!/usr/bin/env python3

"""
Simple pagination
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and end index of a given page and page size.

    Args:
      page (int): The page number.
      page_size (int): The number of items per page.

    Returns:
      Tuple[int, int]: A tuple containing the start and end index of the page.

    Example:
      >>> index_range(1, 10)
      (0, 10)
      >>> index_range(2, 10)
      (10, 20)
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
          page (int): The page number to retrieve. Defaults to 1.
          page_size (int): The number of items per page. Defaults to 10.

        Returns:
          List[List]: The data for the specified page.

        Raises:
          AssertionError: If `page` is not a positive
          integer or `page_size` is not a positive integer.

        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
