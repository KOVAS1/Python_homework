'''
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
функции currency_rates(). Убедиться, что ничего лишнего не происходит.
'''
import dz_4_utils

dz_4_utils.show_currency_rates('eur')
print(*dz_4_utils.currency_rates('brl'))
print(*dz_4_utils.currency_rates('usd'))
print(dz_4_utils.currency_rates('rub'))
dz_4_utils.show_currency_rates('gbp')
print(dz_4_utils.currency_rates('22'))
