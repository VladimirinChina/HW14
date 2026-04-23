import pytest

from src.models import Category, Product
from src.utils import load_data_from_json


@pytest.fixture
def product() -> Product:
    return Product("iPhone", "Smartphone", 999.99, 5)


def test_product_init(product: Product) -> None:
    """Проверка корректной инициализации Product."""
    assert product.name == "iPhone"
    assert product.description == "Smartphone"
    assert product.price == 999.99
    assert product.quantity == 5


def test_category_init_with_products(product: Product) -> None:
    """Проверка создания категории с товарами."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Phones", "Smartphones", [product])

    assert category.name == "Phones"
    assert category.description == "Smartphones"
    assert len(category.products) == 1
    assert isinstance(category.products[0], Product)

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_init_without_products() -> None:
    """Проверка создания категории без передачи списка товаров."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Empty", "No products")

    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_count_multiple() -> None:
    """Проверка подсчета количества категорий."""
    Category.category_count = 0

    Category("A", "desc")
    Category("B", "desc")

    assert Category.category_count == 2


def test_product_count_multiple() -> None:
    """Проверка подсчета количества товаров."""
    Category.product_count = 0

    p1 = Product("A", "desc", 10.0, 1)
    p2 = Product("B", "desc", 20.0, 2)

    Category("Cat1", "desc", [p1, p2])

    assert Category.product_count == 2


def test_products_property_readonly(product: Product) -> None:
    """Проверка, что products доступен через property."""
    category = Category("Test", "Desc", [product])

    assert isinstance(category.products, list)
    assert isinstance(category.products[0], Product)


def test_load_real_json() -> None:
    categories = load_data_from_json("data/products.json")

    assert len(categories) == 2

    # первая категория
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3

    # вторая категория
    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1

    # проверка типов
    assert isinstance(categories[0], Category)
    assert isinstance(categories[0].products[0], Product)
