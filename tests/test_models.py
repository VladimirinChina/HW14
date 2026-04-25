import pytest
from _pytest.capture import CaptureFixture

from src.models import Category, Product


@pytest.fixture
def product() -> Product:
    return Product("Смартфон", "Описание смартфона", 100000.0, 10)


@pytest.fixture
def category(product: Product) -> Category:
    # обнуляем счетчики перед тестами (ВАЖНО!)
    Category.category_count = 0
    Category.product_count = 0
    return Category("Категория", "Описание категории", [product])


# ---------- Product ----------

def test_product_initialization() -> None:
    product = Product("Телефон", "Мобильный телефон", 50000.0, 3)

    assert product.name == "Телефон"
    assert product.description == "Мобильный телефон"
    assert product.price == 50000.0
    assert product.quantity == 3


def test_price_setter_valid() -> None:
    product = Product("Телефон", "Описание", 50000.0, 3)

    product.price = 60000.0
    assert product.price == 60000.0


def test_price_setter_invalid(capsys: CaptureFixture[str]) -> None:
    product = Product("Телефон", "Описание", 50000.0, 3)

    product.price = -100

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0


def test_new_product_create() -> None:
    data = {
        "name": "Телефон",
        "description": "Описание",
        "price": 50000.0,
        "quantity": 3,
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Телефон"


def test_new_product_merge() -> None:
    existing = [Product("Телефон", "Старое описание", 40000.0, 2)]

    data = {
        "name": "Телефон",
        "description": "Новое описание",
        "price": 50000.0,
        "quantity": 3,
    }

    product = Product.new_product(data, existing)

    assert product.quantity == 5  # 2 + 3
    assert product.price == 50000.0  # max


# ---------- Category ----------

def test_category_initialization(category: Category) -> None:
    assert category.name == "Категория"
    assert category.description == "Описание категории"

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_product(category: Category) -> None:
    new_product = Product("Ноутбук", "Игровой ноутбук", 150000.0, 2)

    category.add_product(new_product)

    assert Category.product_count == 2
    assert "Ноутбук" in category.products


def test_products_getter(category: Category) -> None:
    result = category.products

    assert isinstance(result, str)
    assert "Смартфон" in result
    assert "руб." in result
    assert "Остаток" in result


def test_multiple_categories_count() -> None:
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар1", "Описание", 1000, 1)
    p2 = Product("Товар2", "Описание", 2000, 2)

    Category("Категория1", "Описание", [p1])
    Category("Категория2", "Описание", [p2])

    assert Category.category_count == 2
    assert Category.product_count == 2
