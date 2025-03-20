from itertools import product

import pytest

from src.products import Product
from src.category import Category


@pytest.fixture
def product_one():
    return Product(
        name="Iphone 15",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=8,
    )


@pytest.fixture
def product_two():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="512GB, Gray space",
        price=210000.0,
        quantity=14,
    )


@pytest.fixture
def category_one():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        products=[
            Product("Iphone 15", "256GB, Серый цвет, 200MP камера", 180000.0, 8),
            Product("Xiaomi Redmi Note 11", "512GB, Gray space", 210000.0, 14),
        ],
    )


@pytest.fixture
def category_two():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
        products=[
            Product("55 OLED 4K", "Фоновая подсветка", 123000.0, 7),
        ],
    )
