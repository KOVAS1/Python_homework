'''
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

'''
import sys
print('EX#5')
# для вызова задания #5 набрать: python dz_6-5.py dz_6_users.csv dz_6_hobby.csv users_hobby5.txt

f_name1 = sys.argv[1]  # dz_6_users.csv
f_name2 = sys.argv[2]  # dz_6_hobby.csv
f_name3 = sys.argv[3]  # users_hobby5.txt
with open(f_name1, 'r',  encoding='utf-8') as f1,\
        open(f_name2, 'r',  encoding='utf-8') as f2,\
        open(f_name3, 'w',  encoding='utf-8') as f3:

    for line1 in f1:
        line2 = f2.readline().strip()
        if not line2:
            line2 = None
        # print(line1, line2)
        f3.write(f'{line1.strip()}:{line2}\n')
    content = f2.readline()
    if content:
        sys.exit(1)  # выход из Python

print('Задание №5-OK')
