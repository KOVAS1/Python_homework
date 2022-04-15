'''
5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
'''
from time import perf_counter
from sys import getsizeof

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список:{src}')
# решение «в лоб»
start = perf_counter()
unique = [x for x in src if src.count(x) == 1]
print(f'Список «в лоб»:{unique}', type(unique))
print('Время-«в лоб»:', perf_counter() - start)
print('Память-«в лоб»:', getsizeof(unique))

# оптимизация по времени
start = perf_counter()
list_uniq = []
list_temp = []


for el in src:
    if el in list_temp:
        continue
    if el in list_uniq:
        list_temp.append(el)
        list_uniq.remove(el)
        continue
    list_uniq.append(el)
print(f'Список без повторов:{list_uniq}', type(list_uniq))

print('Время-optim:', perf_counter() - start)
print('Память-optim:', getsizeof(list_uniq))
