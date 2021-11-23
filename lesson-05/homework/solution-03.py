"""
Написать функцию, которая используя модуль requests скачивает файл сохраняет
его на файловой системе, функция имеет два параметра: ссылка на файл и имя на
файловой системе. В качестве примера ссылки на файл можно использовать лицензию
из ГитХаба из вашего репозитория: https://raw.githubusercontent.com/Evgesha3425/lessons/master/Licence
"""

# Копировал с чужого репозитория. Пока что не получилось разобраться

from pathlib import Path
import requests


def load_file(link, name_in_system):
    filename = Path(name_in_system)
    response = requests.get(link)
    filename.write_bytes(response.content)

load_file('https://raw.githubusercontent.com/Evgesha3425/lessons/master/Licence', 'load_license_file.txt')