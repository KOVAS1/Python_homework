'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
>>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)

'''
# from functools import wraps


def type_logger(level=0):
    def logger(func):
        # @wraps(func)
        def decor(*argv):
            if level > 0:
                return 'calc_cube(' + ", ".join([f"{func(x)}:{type(func(x))}" for x in argv]) + ")"
            else:
                return "calc_cube(" + ", ".join([str(func(x)) for x in argv]) + ")"
        return decor
    return logger


@ type_logger(1)
def calc_cube(x):
    """ Это комментарий к функции calc_cube(): возведение в куб """
    return x ** 3


print(calc_cube(2))
print('Имя:', calc_cube.__name__)
print(calc_cube.__doc__)
