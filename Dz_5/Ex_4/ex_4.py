'''
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего, например:

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
сделать оптимизацию кода по памяти, по скорости.
'''

from time import perf_counter
from sys import getsizeof
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
print(list(result))
print('Время-0:', perf_counter() - start)
print('Память-0:', getsizeof(result))


# Оптимизация по памяти

start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
result = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])
print('Результат:', *result)
print('Время-m:', perf_counter() - start)
print('Память-m:', getsizeof(result))

# Оптимизация по скорости

start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
result = [src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1]]
print('Результат:', result)
print('Время-s:', perf_counter() - start)
print('Память-s:', getsizeof(result))

