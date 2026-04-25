from src.iterators import CategoryIterator
from src.models import Category, Product


def test_category_iterator() -> None:
    p1 = Product("Товар1", "Описание", 1000, 1)
    p2 = Product("Товар2", "Описание", 2000, 2)

    category = Category("Категория", "Описание", [p1, p2])

    iterator = CategoryIterator(category)

    result = [product.name for product in iterator]

    assert result == ["Товар1", "Товар2"]


def test_get_products_list() -> None:
    p1 = Product("Товар1", "Описание", 1000, 1)
    category = Category("Категория", "Описание", [p1])

    products = category.get_products_list()

    assert isinstance(products, list)
    assert products[0].name == "Товар1"
