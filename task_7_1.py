"""Написать скрипт, создающий стартер (заготовку)
для проекта с заданной структурой папок"""

import os

structure = [
    '|--my_project',
    '   |--settings',
    '   |--mainapp',
    '   |--adminapp',
    '   |--authapp'
]  # в первом приближении храню структуру в списке
a = 1 + 7
dir_path = ''  # первый элемент считаю априори родительским каталогом
lvl = 0
for el in structure:
    # уровень вложенности кратен кол-ву пробелов в начале
    if lvl < (len(el) - len(el.lstrip(' '))) / 3:
        # если увеличился, исправляю-дополняю путь
        lvl = (len(el) - len(el.lstrip(' '))) / 3
        dir_path = os.path.join(dir_path, structure[structure.index(el) - 1].lstrip()[3:])
    elif lvl > (len(el) - len(el.lstrip(' '))) / 3:
        # надо вернуться на уровень выше
        dir_path, _ = os.path.split(dir_path)
        lvl = (len(el) - len(el.lstrip(' '))) / 3
    dir_name = el.lstrip()[3:]
    try:  # перехват случая, когда создаваемая папка уже существует
        os.mkdir(os.path.join(dir_path, dir_name))
    except FileExistsError as e:
        print(f'Каталог {dir_name} не был создан, поскольку уже существует в соответствующем распололжении')
