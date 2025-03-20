def test_category(category_one, category_two):
    assert category_one.name == "Смартфоны"
    assert category_two.name == "Телевизоры"
    assert len(category_one.products) == 2

    assert category_one.category_count == 2
    assert category_two.category_count == 2

    assert category_one.product_count == 3
    assert category_two.product_count == 3
