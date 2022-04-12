'''
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API
в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа,
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? См. https://metanit.com/python/tutorial/6.4.php
Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро.
'''
import requests
from decimal import Decimal


def currency_rates(currency_code):
    response = requests.get(r'http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for el in content.split('<CharCode>')[1:]:
        char_code = el[:3]
        value = (el.split('<Value>')[1:][0].split('</Value>')[0])
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        nominal = Decimal(el.split('<Nominal>')[1:][0].split('</Nominal>')[0])
        course = value / nominal
        val = 'rub'
        if currency_code.upper() == char_code:
            return print(str(f'Курс {char_code}:'), round(float(course), 2), val)


print(currency_rates('gbp'))

