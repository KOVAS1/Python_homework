'''
Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''
import re
print('#8-1')

VALID_RE = re.compile(
    r"(?P<username>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)")


def email_parse(address):
    """ validation of email """
    try:
        test = list(map(lambda x: x.groupdict(), VALID_RE.finditer(address)))
        print(test[0])
    except:
        raise ValueError from ValueError


email_parse('someone@geekbrais.ru')
