'''
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
ОЗУ(разумеется, не нужно реально создавать такие большие файлы, это просто задел на
    будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
сохранить объединенные данные в новый файл(users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
Иванов, Иван, Иванович: скалолазание, охота
Петров, Петр, Петрович: горные лыжи

'''
from itertools import zip_longest
import sys
import os
print('EX#4')


def gen_reader(user_pth, hobby_pth):
    with open(user_pth, "r", encoding="utf-8") as user_f, open(hobby_pth, "r", encoding="utf-8") as hobby_f:
        for user, hobby in zip_longest(user_f, hobby_f):
            # .removesuffix("\n")
            yield (user, hobby if hobby else None)


def groping(output_pth, user_pth, hobby_pth):

    # test of exists files
    if not (os.path.isfile(user_pth) or
            os.path.isfile(hobby_pth)):
        return -1

    with open(output_pth, "w", encoding="utf-8") as out_file:
        for line in gen_reader(user_pth, hobby_pth):
            print(f"{line[0]}: {line[1]}", file=out_file)

    return 0


if __name__ == "__main__":

    user_name = ""
    hobby_name = ""
    output_name = ""

    if len(sys.argv[1:]) >= 3:
        user_name = sys.argv[1]
        hobby_name = sys.argv[2]
        output_name = sys.argv[3]

    if not user_name:
        user_name = "./dz_6_users.csv"
        print('dz_6_users.csv OK!')

    if not hobby_name:
        hobby_name = "./dz_6_hobby.csv"
        print('dz_6_hobby.csv OK!')

    if not output_name:
        output_name = "./dz_6_out.txt"
        print('All OK! , смотри файл dz_6_out.txt')

# exit(groping(user_pth=user_name, hobby_pth=hobby_name, output_pth=output_name)) #выход из выполнения файла

# второй вариант
print('Второй вариант')

with open('dz_6_users.csv', 'r',  encoding='utf-8') as f1, \
        open('dz_6_hobby.csv', 'r', encoding='utf-8') as f2,\
        open('users_hobby.txt', 'w', encoding='utf-8') as f3:
    for line1 in f1:
        line2 = f2.readline().strip()
        if not line2:
            line2 = None
        f3.write(f'{line1.strip()}:{line2}\n')
    content = f2.readline()
    print(type(content), 'Создан файл, смотри users_hobby.txt')
    if content:
        sys.exit(1)

# третий вариант
print('Третий вариант, - смотри: users_hobby3.txt')

with open('dz_6_users.csv', 'r',  encoding='utf-8') as in_1, \
        open('dz_6_hobby.csv', 'r', encoding='utf-8') as in_2,\
        open('users_hobby3.txt', 'w', encoding='utf-8') as out:
    for hobbies, user in zip(in_2, in_1):
        out.write(f'{user.strip()}:{hobbies.strip()}\n')
    for user in in_1:
        out.write(f'{user.strip()}:{None}\n')
