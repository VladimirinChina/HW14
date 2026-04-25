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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """
        Геттер цены.

        :return: текущая цена товара
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер цены с валидацией.

        :param value: новая цена
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            user_answer = input(f"Цена товара {self.name} понижается. Вы уверены? (y/n): ")
            if user_answer.lower() == "y":
                print("Операция выполнена.")
                return

        self.__price = value

    @classmethod
    def new_product(cls, data: dict, existing_products: Optional[List["Product"]] = None) -> "Product":
        """
        Создает продукт или обновляет существующий.
        """
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        # Доп. задание: логика объединения дубликатов
        if existing_products:
            for product in existing_products:
                if product.name == name:
                    # Складываем количество
                    product.quantity += quantity
                    # Выбираем максимальную цену
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)


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

    def add_product(self, product: Product) -> None:
        """
        Добавляет новый продукт в категорию.

        Продукт добавляется в приватный список товаров категории.
        При добавлении увеличивается общий счетчик товаров (product_count).
        :param product: Объект продукта, который необходимо добавить в категорию
        :return: None
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        # Используем список для сборки строк (более эффективно, чем +=)
        product_list = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]
        return "\n".join(product_list) + "\n"
