'''

1. Не используя библиотеки для парсинга, распарсить(получить определённые данные) файл логов web-сервера nginx_logs.txt
(https: // github.com/elastic/examples/raw/master/Common % 20Data % 20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида:
( < remote_addr > , < request_type > , < requested_resource > ). 

Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]

'''


print('EX#1')
# прочитать файл


with open('dz_6_nginx_logs.txt', 'r',  encoding='utf-8') as f:
    f_new = []
    for i in f:
        el = i.split()
        f_new.append((el[0], el[5].strip('"'), el[6]))
f_new1 = tuple(f_new)
print(type(f_new1), f_new1[:3])

# data = []
# row_data = []


# with open('dz_6_nginx_logs.txt', 'r', encoding='utf-8') as file:
#     for num, row in enumerate(file):
#         raw_row = row.split()
#         print("RAW", raw_row, "ROW")
#         row_data = [raw_row[0], raw_row[5].strip('"'), raw_row[6]]
#         data.append(tuple(row_data))
#         if num == 2:
#             break
# print(data)
