from typing import Any

import pytest

from src.models import Category, LawnGrass, Smartphone


def test_smartphone_initialization() -> None:
    smart = Smartphone("Samsung", "S23", 100000.0, 5, 95.5, "S23 Ultra", 256, "Gray")
    assert smart.name == "Samsung"
    assert smart.memory == 256


def test_lawngrass_initialization() -> None:
    grass = LawnGrass("Трава", "Зеленая", 500.0, 20, "Russia", "7 days", "Green")
    assert grass.country == "Russia"


def test_product_add_different_classes() -> None:
    smart = Smartphone("Samsung", "S23", 100000.0, 2, 95.5, "S23 Ultra", 256, "Gray")
    grass = LawnGrass("Трава", "Зеленая", 500.0, 10, "Russia", "7 days", "Green")

    # Должна возникнуть ошибка при сложении разных классов
    with pytest.raises(TypeError):
        smart + grass


def test_product_add_same_classes() -> None:
    smart1 = Smartphone("Samsung", "S23", 100.0, 2, 95.5, "S23 Ultra", 256, "Gray")
    smart2 = Smartphone("Iphone", "15", 200.0, 3, 98.2, "15", 512, "Silver")
    # (100 * 2) + (200 * 3) = 200 + 600 = 800
    assert smart1 + smart2 == 800.0


def test_category_add_invalid_object() -> None:
    category = Category("Тест", "Описание")
    invalid_data: Any = "Не продукт"  # type ignore
    # Нельзя добавлять строки
    with pytest.raises(TypeError):
        category.add_product(invalid_data)
