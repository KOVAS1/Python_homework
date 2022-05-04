'''
7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров. 
Проверить корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма: {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        return f'Произведение: {self.a * other.a - (self.b * other.b)} + {self.b * other.a +self.a * other.b} * j'


a1, b1 = 5, -8
a2, b2 = 3, 15

c_1 = ComplexNumber(a1, b1)
c_2 = ComplexNumber(a2, b2)

print(f'Число_1=({a1}+{b1}*j); Число_2=({a2}+{b2}*j)')

print(c_1 + c_2)
print(c_1 * c_2)

print(
    f'Проверка: {complex(a1, b1)+complex(a2, b2)}; {complex(a1, b1)*complex(a2, b2)}')
