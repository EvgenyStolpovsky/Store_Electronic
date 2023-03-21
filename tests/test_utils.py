import pytest
from store.utils import Item, Phone, KeyBoard

def test__init_item__():
    """инициализация экземпляра класса"""
    item1 = Item('Xiaomi Lite 10', 30_000, 10)
    assert item1.name == "Xiaomi Lite 10"
    assert item1.price == 30_000
    assert item1.count == 10

def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 100_000

def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False

def test__repr__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__repr__() != Item('Смартфон', '10000', '20')

def test__str__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__str__() != Item('Смартфон', 10000, 20)

def test__init_phone__():
    """инициализация экземпляра класса"""
    phone1 = Phone('Iphone 14', 120_000, 5, 2)
    assert phone1.name == "Iphone 14"
    assert phone1.price == 120_000
    assert phone1.count == 5

def test__add__():
    """Сложение экземпляров классов (количество товара - count)"""
    item1 = Item('Xiaomi Lite 10', 30_000, 10)
    phone1 = Phone('Iphone 14', 120_000, 5, 2)
    assert item1.__add__(phone1) == 15
    assert item1.count + phone1.price != ValueError

def test__init__():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.count == 5

def test_KeyBoard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'
    assert kb.change_lang() != 'RU'