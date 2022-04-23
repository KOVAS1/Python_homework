'''
2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения <request_type>, информации вида:
<requested_resource>, (<remote_addr>, <response_code>, <request_datetime>, <response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
/downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
'/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
'''
import re

pattern = re.compile(
    r'(?P<addres>^((\d|[a-fA-F]){0,4}[\.\:]?){4,8})[\s-]*\[(?P<datatime>.*)\]\s*\"(?P<req>\w*)\s*(?P<file>[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)')


# в файле 8-2_nginx_logs.txt уменьшено количество строк, при выводе на печать - меньше листать.
with open("./8-2_nginx_logs.txt", "r", encoding="utf-8") as file:
    for line in file:
        for i in pattern.finditer(line):
            print(i.groupdict())
