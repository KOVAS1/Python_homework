'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. 
Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
'''


class Date:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extract_date(cls, data):
        day, month, year = [int(i) for i in data.split('-')]
        if day < 32 and month < 13 and len(str(year)) == 4:
            return f"День {day, type(day)}\n\rМесяц {month, type(month)}\n\rГод  {year, type(year)}"
        else:
            print('Ошибка ввода данных. Введите дату правильно "dd-md-yyyy"!')

    @staticmethod
    def validation(data):
        day, month, year = map(int, data.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year != 0 and len(str(year)) == 4:
            print(f'Дата валидна: {data}')
            # return day, month, year
        elif day > 31:
            print('День введен неверно!')
        elif month > 12:
            print('Месяц введен неверно!')
        else:
            print('Год введен неверно!')


my_date = '12-04 -2022'
print(f'Дата: {my_date}')
print(Date.extract_date(my_date))
Date.validation(my_date)
# print(Date.validation(my_date))
