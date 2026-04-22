from typing import List, Optional


class Product:
    """
    Класс, представляющий товар.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация объекта товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price})"


class Category:
    """
    Класс, представляющий категорию товаров.
    """
    # Атрибуты класса для хранения общего счетчика
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Инициализация объекта категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров категории
        """
        self.name = name
        self.description = description
        # Защита: если список не передан, создаем пустой, чтобы не было ошибки len()
        self.__products = products if products is not None else []

        # Автоматическое заполнение атрибутов класса согласно заданию
        Category.category_count += 1
        # Считаем количество уникальных позиций товаров в этой категории
        Category.product_count += len(self.__products)

    @property
    def products(self) -> List[Product]:
        """Геттер для списка продуктов."""
        return self.__products
