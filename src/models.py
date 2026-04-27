from abc import ABC, abstractmethod
from typing import List, Optional, Any


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        """
        Инициализация объекта товара.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """
        Абстрактный метод строкового представления.
        """
        pass


class BaseEntity(ABC):
    """
    Абстрактный класс для сущностей, работающих с продуктами.
    """
    @abstractmethod
    def total_cost(self) -> float:
        """Возвращает общую стоимость."""
        pass


class PrintMixin:
    """
    Миксин для вывода информации о создании объекта.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        attrs = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attrs})"


class Product(PrintMixin, BaseProduct):
    """
    Класс, представляющий товар.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """
        Строковое представление товара.

        :return: строка вида:
        "Название продукта, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Складывает два товара (их полную стоимость на складе).

        :param other: второй товар
        :return: сумма (price * quantity) для двух товаров
        """
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты Product")

        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        """
        Геттер цены.

        :return: текущая цена товара
        """
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер цены с валидацией.

        :param value: новая цена
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self._price:
            user_answer = input(f"Цена товара {self.name} понижается. Вы уверены? (y/n): ")
            if user_answer.lower() == "y":
                print("Операция выполнена.")
                return

        self._price = value

    @classmethod
    def new_product(cls, data: dict, existing_products: Optional[List["Product"]] = None) -> "Product":
        """
        Создает продукт или обновляет существующий.
        """
        #  Поиск дубликатов
        if existing_products:
            for product in existing_products:
                if product.name == data["name"]:
                    # Складываем количество
                    product.quantity += data["quantity"]
                    # Выбираем максимальную цену
                    if data["price"] > product.price:
                        product.price = data["price"]
                    return product

        return cls(**data)


class Smartphone(Product):
    """Класс для смартфонов."""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """
        Инициализация объекта товара.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        :param efficiency: производительность
        :param model: модель
        :param memory: объем внутренней памяти
        :param color: цвет
        """
        # Вызываем конструктор родителя для общих полей
        super().__init__(name, description, price, quantity)
        # Добавляем специфические поля
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы."""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Инициализация объекта товара
        :param name: название товара
        :param description: описание товара
        :param price: цена товара
        :param quantity: количество товара в наличии
        :param country: страна-производитель
        :param germination_period: срок прорастания
        :param color: цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category(BaseEntity):
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

    def __str__(self) -> str:
        """
        Строковое представление категории.

        :return: строка вида:
        "Название категории, количество продуктов: X шт."
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

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

    def total_cost(self) -> float:
        """Общая стоимость всех товаров в категории."""
        return sum(product.price * product.quantity for product in self.__products)

    def get_products_list(self) -> List[Product]:
        """
        Возвращает список продуктов категории.
        (внутренний метод для служебного использования)
        """
        return self.__products

    @property
    def products(self) -> str:
        # Используем список для сборки строк (более эффективно, чем +=)
        product_list = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]
        return "\n".join(product_list) + "\n"


class Order(BaseEntity):
    """
    Класс заказа (один товар).
    """

    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def total_cost(self) -> float:
        """
        Общая стоимость заказа.
        """
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.product.name}, {self.quantity} шт. = {self.total_cost()} руб."
