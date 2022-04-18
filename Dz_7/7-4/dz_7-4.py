'''
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

'''

import sys
import os

# Вариант1 - для запуска набирать: python dz_7-4.py some_data
#import sys
#import os

size_f = {}


def scan_mem(pth):
    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:
        for node in files:
            if os.path.isfile(node):
                mem = 10 ** len(str(os.stat(node).st_size))
                size_f[mem] = size_f.get(mem, 0)+1
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()

    scan_mem(pth)
    print(size_f)

# Вариант2 - предпочтителен, не надо набирать имя папки (some_data)в командной строке при запуске программы
print('вариант2')
# import os
ROOT = os.path.dirname(__file__)
data_path = os.path.join(ROOT, 'some_data')

result = {0: 0, 10: 0, 100: 0, 1000: 0,
          10000: 0, 10000: 0, 100000: 0}
keys = [0, 10, 100, 1000, 10000, 100000]

for root, dirs, files in os.walk(data_path):
    for _ in files:
        size_f = os.stat(os.path.join(root, _)).st_size
        if size_f == 0:
            result[0] += 1
            continue
        for ind, key in enumerate(keys):
            if ind == len(keys)-1:
                print(f'Слишком большой файл{_}')
                break
            if key < size_f <= keys[ind+1]:
                result[keys[ind+1]] += 1
                break
print(result)
