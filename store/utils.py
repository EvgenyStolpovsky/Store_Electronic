import csv

class InstantiateCSVError(Exception):
    pass

class Item:
    pay_rate = 1
    all = []

    def __init__(self, name: object, price: object, count: object) -> object:
        """Название товара, цена за единицу и количество товара в магазине"""
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

    def calculate_total_price(self) -> int:
        """Общая стоимость товара"""
        return self.price * self.count

    def apply_discount(self) -> int:
        """Скидка для товара"""
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        try:
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
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except:
            raise InstantiateCSVError('Файл items.csv поврежден')

    @staticmethod
    def is_integer(num):
        if num - int(num) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.count}')"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        """Сложение количества товара. """
        if isinstance(other, Item):
            return self.count + other.count
        else:
            raise ValueError('Сложение с другими аргументами класса запрещено')

class Phone(Item):
    """Класс телефон, наследственный класс."""

    def __init__(self, name, price, count, sim_kart):
        """Инициализация нового атрибута - количество сим карт."""
        super().__init__(name, price, count)
        self.__sim_kart = sim_kart
        if sim_kart == 0:
            raise ValueError('Количество физических Sim карт должно быть целым число больше нуля.')
        else:
            self.__sim_kart = sim_kart

class MixinLog:
    def __init__(self, name, price, count):
        """Иницализация названия, стоимости и кол-во клавиатуры,"""
        self.__language = 'EN'
        super().__init__(name, price, count)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Изменение языка раскладка клавиатуры EN - RU"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

class KeyBoard(MixinLog, Item):
    """Клавиатура новый товар"""
    pass



# Файл items.csv отсутствует.
Item.instantiate_from_csv()
print(Item.all)
# FileNotFoundError: Отсутствует файл item.csv

# В файле items.csv удалена последняя колонка.
Item.instantiate_from_csv()
# InstantiateCSVError: Файл item.csv поврежден


item1 = Item('Xiaomi Lite 10', 30_000, 10)
phone1 = Phone('Iphone 14', 120_000, 5, 5)
kb = KeyBoard('Dark Project KD87A', 9600, 5)

# ДЗ 15.2
# print(kb) # Dark Project KD87A.
# print(kb.language) # EN.
# kb.change_lang()
# print(kb.language) # RU.

# ДЗ 14.2
print(phone1) # Iphone 14.
print(repr(phone1)) # Item('Iphone 14', '120000', '5').
print(repr(item1)) # Item('Xiaomi Lite 10', '30000', '10').
print(phone1 + item1) # 15


