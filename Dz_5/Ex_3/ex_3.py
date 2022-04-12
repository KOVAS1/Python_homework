'''
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида ( < tutor > , < klass > ),
например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (< tutor > , None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''

from itertools import zip_longest
#.zip_longest() работает пока самая длинная итерация не будет исчерпана, а пропущенные элементы заполняются значением fillvalue=None.


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена', ]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9Г']

tutor_klass_dict = {i: j for i, j in zip_longest(
    tutors, klasses)}  # в виде словаря
tutor_klass_tuple = ((i, j) for i, j in zip_longest(tutors, klasses))
# tutor_klass = tuple(tutor_klass)
print(type(tutor_klass_dict), tutor_klass_dict)
print(type(tutor_klass_tuple))
for i in tutor_klass_tuple:
    print(i)

print('\n next\n')

from itertools import zip_longest
TUTORS = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена', 'Serge', 'Bob']
KLASSES = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9Г']


def klass_tutor_gen():
    for tutor, klass in zip_longest(TUTORS, KLASSES):
        if tutor is None:
            break
        yield tutor, klass


klass_tutor = klass_tutor_gen()
print(type(klass_tutor))
for el in klass_tutor:
    print(el)

