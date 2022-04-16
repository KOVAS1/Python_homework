'''
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов
код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.

'''
from collections import Counter
print('EX#2')
f_new2 = []  # пустой список -list
d = dict()  # пустой словарь
with open('dz_6_nginx_logs.txt', 'r',  encoding='utf-8') as f:
    for i in f:
        el = i.split()
        ip = el[0]
        f_new2.append((ip))  # el[5].strip('"'), el[6]
        if ip not in d:
            d[ip] = 1
        else:
            d[ip] += 1
# print(type(d), f_new2[:3])
# print(d['216.46.173.126'])

k = ''  # spammer IP
m = 0  # число запросов
for key, value in d.items():
    if value > m:
        m = value
        k = key
print('spammer`s IP:', k, 'Запросов:', m)
# Вариант решения №2
#from collections import Counter
with open('dz_6_nginx_logs.txt', 'r',  encoding='utf-8') as f:
    base = [el.split()[0]for el in f]
ip, count = Counter(base).most_common(1)[0]

print(f'IP:{ip}, count:{count}')
