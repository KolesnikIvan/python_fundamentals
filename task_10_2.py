import random
import string
from abc import ABC, abstractmethod

class Clothes:
    """Основная сущность (класс) — одежда.

      Может иметь определённое название.
      У типов одежды параметр: размер (для пальто) или рост (для костюма).
      """
    def __init__(self, name, measure):
        self.name = str(name)
        self.measure = float(measure)

    def __str__(self):
        return self.name + ' ' + str(self.measure)

    def __add__(self, other):
        a = self.textile_expenditure()
        b = other.textile_expenditure()
        return Clothes(f'{self.name}+{other.name}', a + b)

    def __radd__(self, other):
        return self.__add__(other)

    @property
    @abstractmethod
    def textile_expenditure(self):
        """Абстрактный метод для основных классов проекта"""
        pass


class OverCoat(Clothes):

    def textile_expenditure(self):
        return self.measure/6.5 + 0.5


class Suit(Clothes):

    def textile_expenditure(self):
        return 2 * self.measure + 0.3


class Clothing:
    """Класс предназначен для расчета общего расхода ткани."""
    def __init__(self):
        self.garments = []

    def __str__(self):
        return ', '.join(map(str, self.garments))
        # return ', '.join(self.garments) это не сработало
        # т.к. join хочет только строки на входе

    def add_garment(self, piece_of_clo):
        self.garments.append(piece_of_clo)

    @property
    def total_textile_expenditure(self):
        # total = sum(self.garments)  # вот никак не смог применить здесь sum
        # только увидел, что и в методичке суммирование сделано через цикл
        total = 0
        for el in self.garments:
            total += el.textile_expenditure()
        return total

oc = OverCoat('coat', 13)
st = Suit('suit', 1.85)
print(oc, oc.textile_expenditure())
print(st, st.textile_expenditure())
print(oc + st)  # проверяю перегруженное суммирование объектов

# формируется случайный набор предметов одежды
# для которого впоследствии определяется расход материала
wardrobe = Clothing()
for i in range(random.randint(3, 5)):
    cloth = OverCoat(''.join(random.sample(string.ascii_letters, 3)), random.randint(1, 7)) if random.random() < 0.5 \
        else Suit(''.join(random.sample(string.ascii_letters, 4)), random.randint(1, 7))
    wardrobe.add_garment(cloth)

print(wardrobe)
print(wardrobe.total_textile_expenditure)
