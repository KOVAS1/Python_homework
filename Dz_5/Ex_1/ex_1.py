'''
1. Написать генератор нечётных чисел от 1 до n(включительно), используя ключевое слово
yield, например:
>> > odd_to_15 = odd_nums(15)
>> > next(odd_to_15)
1
>> > next(odd_to_15)
3
...
>> > next(odd_to_15)
15
>> > next(odd_to_15)
...StopIteration...
'''
from sys import getsizeof
from time import perf_counter
from itertools import zip_longest



def odd_nums(args):
    for n in range(1, args + 1, 2):
        yield n


nums = int(input('input number:'))
for num in odd_nums(nums):
    print(num, end=',')

print(type(odd_nums))

