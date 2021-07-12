"""Скрипт, создающий из config.yaml стартер для проекта
со заданной структурой"""
import os

with open('config', 'r', encoding='utf-8') as f:
    dir_path = ''
    lvl = 0
    obj_name = ''
    for line in f:
        idnt = line.strip('\n').find('|-')                       # позиция начала имени в строке
        obj_name_old = obj_name
        obj_name = line.strip('\n')[idnt + 3:]                   # имя очередного объекта структуры
        folder = False if '.' in line else True      # тип: файл или каталог по наличию точки

        if lvl < idnt / 3:
            # если отступ увеличился, исправить путь к каталогу
            dir_path = os.path.join(dir_path, obj_name_old)
            lvl = idnt / 3
        elif lvl > idnt / 3:
            # если уменьшился, вернуть на уровень назад
            # если уменьшился не на одну ступень, повторяю сплит
            for _ in range(int(lvl - idnt/3)):
                dir_path, _ = os.path.split(dir_path)
            lvl = idnt / 3

        if folder:
            try:
                os.mkdir(os.path.join(dir_path, obj_name))
            except FileExistsError:
                print(f'Каталог {obj_name} не был создан, т.к. уже существует по указанному адресу')
        else:
            try:
                f_path = os.path.join(dir_path, obj_name)
                fl = open(f_path, 'x', encoding='utf-8')
                fl.write(f'"""{obj_name}"""')
                fl.close()
            except FileExistsError as e:
                print(f'Файл {obj_name} не был создан, т.к. уже существует по указанному адресу')
