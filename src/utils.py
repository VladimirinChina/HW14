import json
from typing import List

from src.models import Category, Product


def load_data_from_json(path: str) -> List[Category]:
    """
    Загружает категории и товары из JSON-файла.

    :param path: Путь к JSON-файлу
    :return: Список объектов Category
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories: List[Category] = []

    for category_data in data:
        products = []

        for product_data in category_data.get("products", []):
            try:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=float(product_data["price"]),
                    quantity=int(product_data["quantity"]),
                )
                products.append(product)
            except KeyError:
                # если вдруг кривой JSON — просто пропускаем
                continue

        category = Category(
            name=category_data.get("name", "Без названия"),
            description=category_data.get("description", ""),
            products=products,
        )

        categories.append(category)

    return categories
