import csv

class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, count):
        self.__name = name
        self.price = price
        self.count = count
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        self.__name = name

    def calculate_total_price(self):
        return self.price * self.count

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r', encoding='windows-1251') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
            for a in rows[1:len(rows)]:
                if Item.is_integer(float(a[1])):
                    a[1] = int(a[1])
                if Item.is_integer(float(a[2])):
                    a[2] = int(a[2])
                cls(a[0], a[1], a[2])

    @staticmethod
    def is_integer(num):
        if num - int(num) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.__name}, {self.price}, {self.count}'

    def __str__(self):
        return f'{self.name}'
    def __add__(self, other):
        if isinstance(other, Item):
            return self.count + other.count
        else:
            raise ValueError("Сложение с другими аргументами класса запрещено")

class Phone(Item):
    """Класс телефон, наследственный класс"""
    def __init__(self, name, price, count, sim_card):
        """Инициализация нового атрубута- количество сим-карт"""
        super().__init__(name, price, count)
        self.sim_card = sim_card
        if sim_card == 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.sim_card = sim_card

# смартфон iPhone 14, цена 120_000, количетсво товара 5, симкарт 2
phone1 = Phone("iPhone 14", 120_000, 5, 2)
print(phone1)
#iPhone 14

print(repr(phone1))
#Phone('iPhone 14', 120000, 5, 2)

#phone1.number_of_sim = 0
#ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.


item1 = Item("Смартфон", 10_000, 20)
#print(repr(item1)) # Смартфон, 10000, 20
#print(item1) # Смартфон






