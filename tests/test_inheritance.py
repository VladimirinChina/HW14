import pytest

from src.models import BaseProduct, LawnGrass, Product, Smartphone

# ---------- BaseProduct ----------


def test_product_is_instance_of_base() -> None:
    product = Product("Товар", "Описание", 100.0, 5)

    # Проверяем, что Product вообще создается и работает
    assert product.name == "Товар"
    assert product.quantity == 5


def test_product_inherits_base() -> None:
    product = Product("Товар", "Описание", 100.0, 5)

    assert isinstance(product, BaseProduct)

# ---------- Mixin (печать) ----------


def test_mixin_print(capsys: pytest.CaptureFixture[str]) -> None:
    Product("Товар", "Описание", 100.0, 5)

    captured = capsys.readouterr()

    assert "name='Товар'" in captured.out
    assert "quantity=5" in captured.out


def test_repr_format() -> None:
    product = Product("Товар", "Описание", 100.0, 5)

    repr_str = repr(product)

    assert "Product(" in repr_str
    assert "name='Товар'" in repr_str
    assert "quantity=5" in repr_str


# ---------- Smartphone ----------

def test_smartphone_creation() -> None:
    phone = Smartphone(
        "iPhone",
        "Описание",
        100000.0,
        10,
        efficiency=95.5,
        model="15 Pro",
        memory=256,
        color="Black"
    )

    assert phone.name == "iPhone"
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Black"


# ---------- LawnGrass ----------

def test_lawn_grass_creation() -> None:
    grass = LawnGrass(
        "Газон",
        "Зеленый газон",
        500.0,
        20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )

    assert grass.name == "Газон"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


# ---------- Наследование логики Product ----------

def test_inherited_methods() -> None:
    phone = Smartphone(
        "iPhone",
        "Описание",
        100000.0,
        2,
        efficiency=95.5,
        model="15 Pro",
        memory=256,
        color="Black"
    )

    other = Smartphone(
        "Samsung",
        "Описание",
        50000.0,
        1,
        efficiency=90.0,
        model="S23",
        memory=128,
        color="White"
    )

    # Проверяем __add__
    result = phone + other
    assert result == (100000.0 * 2 + 50000.0 * 1)

    # Проверяем __str__
    assert "iPhone" in str(phone)
    assert "руб." in str(phone)
