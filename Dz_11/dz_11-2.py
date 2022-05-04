'''
2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class DivZeroException(Exception):
    text = "Делить на ноль нельзя!"

    def __str__(self):
        return self.text

    @staticmethod
    def divide_by_null():
        d1 = int(input('Введите число: '))
        d2 = int(input('Введите делитель: '))
        if d2 == 0:
            raise DivZeroException

        else:
            result = d1 / d2
            print(f'{result:.2f}')


DivZeroException.divide_by_null()
