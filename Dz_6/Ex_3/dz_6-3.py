'''
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях(users.csv):
Иванов, Иван, Иванович
Петров, Петр, Петрович
Фрагмент файла с данными о хобби(hobby.csv):
скалолазание, охота
горные лыжи

'''

import csv
import json
import sys
import pickle
from itertools import zip_longest
print('EX#3')


users = []
hobbies = []

with open('dz_6_users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        users.append(line.strip())

with open('dz_6_hobby.csv', 'r', encoding='utf-8') as f:
    for line in f:
        hobbies.append(line.strip())

if len(users) < len(hobbies):
    exit(1)

hobbies_of_users = {user: hobby for (
    user, hobby) in zip_longest(users, hobbies)}

with open('hobbies_of_users.pickle', 'wb') as f:
    pickle.dump(hobbies_of_users, f)

with open('hobbies_of_users.pickle', 'rb') as f:
    content = pickle.load(f)

print(type(content))
for el in content.items():
    print(el)

# вариант на скорость чтения
print('Вариант на скорость чтения')

result_dict = {}
with open('dz_6_users.csv', 'r',  encoding='utf-8') as f_1, \
        open('dz_6_hobby.csv', 'r', encoding='utf-8') as f_2:
    users = (el for el in f_1.read().splitlines())
    hobbies_data = (el for el in f_2.read().splitlines())
    for hobbies, user in zip(hobbies_data, users):
        result_dict[user.strip()] = hobbies.strip()
    for _ in hobbies_data:
        sys.exit(1)
    for user in users:
        result_dict[user.strip()] = None
print(result_dict)
with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result_dict, result_file, ensure_ascii=False)
