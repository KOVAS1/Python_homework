import sys

# Набирать в командной строке python add_sale.py 12378
# в конец файла bakery.csv добавится это число - 12378

sales = sys.argv[1]
with open('bakery.csv', 'a',  encoding='utf-8') as f:
    f.write('\n')  # переводит на следующую строку
    f.write(sales)  # записывает 12378 в эту строку
