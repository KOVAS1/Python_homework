'''
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
'''
from abc import abstractmethod


class Textil:
    def __init__(self, size, amount):
        self.size = size
        self.amount = amount

    @abstractmethod
    def get_sq_full(self):
        pass


class Coat(Textil):
    def __init__(self, size, amount):
        super().__init__(size, amount)
        self.square_c = round(self.size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход ткани на 1 пальто {self.square_c} м.\n \rКоличество пальто - {self.amount} шт.'

    @property
    def get_sq_full(self):
        total = self.square_c*self.amount
        return f'Всего ткани на пальто (на {self.amount} шт.) - {total} м.'


class Suit(Textil):
    def __init__(self, size, amount):
        super().__init__(size, amount)
        self.square = round(self.size * 2 + 0.3, 2)

    def __str__(self):
        return f'Расход ткани на 1 костюм {self.square} м.\n \rКоличество костюмов - {self.amount} шт.'

    @property
    def get_sq_full(self):
        total = self.square*self.amount
        return f'Всего ткани на костюмы (на {self.amount} шт.) - {total} м.'


coat = Coat(65, 4)  # размер для пальто (40,42,...65), количество
suit = Suit(2, 10)  # Рост для костюма (1,2,...5), количество

print(coat)
print(suit)

print(coat.get_sq_full)
print(suit.get_sq_full)
