class Item:
    discount = 0.85

    def __init__(self, name, price, quantity):
        """Название товара, цена за единицу, количество товара в магазине"""
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost (self):
        """общая стоимость товара"""
        return self.quantity * self.price

    def price_discount (self):
        """Скидка для товара"""
        return self.price * self.discount


item1 = Item("Смартфон", 10_000, 20)
item1.total_cost()
item1.price_discount
print(item1.name)
print(f'Общая стоимость товара = {item1.total_cost()}')
print(f'Стоимость товара с учетом скидки = {item1.price_discount()}')

item2 = Item("Ноутбук", 20000, 5)
print(item2.name)
item2.total_cost()
print(f'Общая стоимость товара = {item2.total_cost()}')
item2.price_discount()
print(f'Стоимость товара с учетом скидки = {item2.price_discount()}')































#item2 = Item("Ноутбук", 20000, 5)

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
#200000  # общая стоимость смартфонов
#100000  # общая стоимость ноутбуков


#item1.apply_discount()
#print(item1.price)
#print(item2.price)
#8000.0  # к цене смартфона применена скидка
#20000  # к цене ноутбука скидка не была применена

#print(Item.all)
#[<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]