def test_product(product_one, product_two):
    assert product_one.name == "Iphone 15"
    assert product_one.description == "256GB, Серый цвет, 200MP камера"
    assert product_one.price == 180000.0
    assert product_one.quantity == 8
    assert product_two.name == "Xiaomi Redmi Note 11"
    assert product_two.description == "512GB, Gray space"
    assert product_two.price == 210000.0
    assert product_two.quantity == 14
