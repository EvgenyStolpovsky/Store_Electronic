import pytest
from store.utils import Item, Phone, KeyBoard
def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 100_000

def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False

def test__repr__():
    item1 = Item("Смартфон", 10_000, 20)
    assert item1.__repr__() != Item("Смартфон", 10_000, 20)

def test__str__():
    item1 = Item("Смартфон", 10_000, 20)
    assert item1.__str__() != Item("Смартфон", 10_000, 20)

def test__init__Phone():
    """Инициализация экземпляра дочернего класса"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.count == 5

def test__init__():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.count == 5

def test_KeyBoard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    assert kb.change_lang() != "RU"

