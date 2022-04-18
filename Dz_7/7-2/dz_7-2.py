'''
2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
структурой:
|--my_project
|--settings
| |--__init__.py
| |--dev.py
| |--prod.py
|--mainapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
|
|--mainapp
| |--base.html
| |--index.html
|--authapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
|
|--authapp
| |--base.html
| |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.
'''


import json
import os

print('создание структуры проекта из файла config.json')

ROOT = os.path.dirname(__file__)

with open('config.json', 'r', encoding='utf-8') as f:
    conf = json.load(f)
    # print(conf)

for dir_path in conf:
    full_dir_path = os.path.join(ROOT, dir_path)
    os.makedirs(full_dir_path, exist_ok=True)
    for file_name in conf[dir_path]:
        with open(os.path.join(full_dir_path, file_name), 'x', encoding='utf-8'):
            pass
print('.json OK!')
