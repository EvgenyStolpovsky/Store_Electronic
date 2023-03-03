from store.utils import Item

def test_total_cost():
    """Общая стоимость товара"""
    item1 = Item("Смартфон", 10_000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.total_cost() == 200_000
    assert item2.total_cost() == 100_000

def test_price_discount():
    """Скидка для товара"""
    item1 = Item("Смартфон", 10_000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.price_discount() == 8500.0
    assert item2.price_discount() == 17000.0


