from typing import Iterator

from src.models import Category, Product


class CategoryIterator:
    """
    Итератор для перебора товаров категории.

    Позволяет использовать объект в цикле for.
    """

    def __init__(self, category: Category) -> None:
        """
        Инициализация итератора.

        :param category: объект категории
        """
        self._products = category.get_products_list()

    def __iter__(self) -> Iterator[Product]:
        """
        Возвращает генератор товаров.

        :return: итератор по товарам категории
        """
        for product in self._products:
            yield product
