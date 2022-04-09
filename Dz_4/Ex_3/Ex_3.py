'''
3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?'''
from datetime import date

import requests
from decimal import Decimal

def currency_rates(currency_code=None):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    cur_date = content.split('Date="')[1][:10].split('.')
    cur_date = date(day=int(cur_date[0]), month=int(
        cur_date[1]), year=int(cur_date[2]))
    for el in content.split('<CharCode>')[1:]:
        char_code = el[:3]
        value = (el.split('<Value>')[1:][0].split('</Value>')[0])
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        nominal = Decimal(el.split('<Nominal>')[1:][0].split('</Nominal>')[0])
        if str(currency_code).upper() == char_code:
            return print(f'На {cur_date} курс {str(char_code)}: {round(float(value/nominal), 2)} руб.')


print(currency_rates('usd'))
currency_rates('gbp')
print(currency_rates('AMD'))
# print(currency_rates('rub'))
# print(currency_rates(12))
# print(currency_rates())
# print(*currency_rates('usd'))
