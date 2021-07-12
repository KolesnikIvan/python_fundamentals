"""Cкрипт, который собирает все шаблоны в одну папку templates"""
import os
import shutil

# root_sir = r'.\my_project'
root_dir = os.path.join('.', 'my_project')      # корень проекта
target_dir = os.path.join(root_dir, 'TMPLTS')   # папка, куда следует копировать
# создается целевая папка; старая папка templates в корне удаляется
if os.path.exists(os.path.join(root_dir, 'templates')):
    shutil.rmtree(os.path.join(root_dir, 'templates'))
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

for root, dirs, files in os.walk(root_dir):
    if 'template' in root:
        for dr in dirs:
            try:
                # если в корне есть слово template
                # то подпапки этого каталога воспроизводятся в целевой
                copy_dr = os.path.join(target_dir, dr)
                os.mkdir(copy_dr)
            except Exception as e:
                print(f'Folder {dr} was not created. {e}')

            # также и файлы из подпапок template копируются в целевую
            for item in os.scandir(os.path.join(root, dr)):
                try:
                    shutil.copy(item.path, os.path.join(copy_dr, item.name))
                except Exception as e:
                    print(f'File {item.name} was not copied. {e}')

# целевая папка переименовывается, как требуется
os.renames(target_dir, os.path.join(root_dir, 'templates'))

# вижу, что сделал копирование только из подпапок и только "первого уровня"
# а как делают профессионалы?
# такое количество перехватов, условий и вложенных циклов
# не похоже на pythonic way, если я правильно понимаю


# Первоначалбно копировал только файлы (вариант ниже)
# но они заменяли друг друга, поскольку одинаково называются
# for root, _, files in os.walk(root_dir):
#     for fl in files:
#         if 'template' in root and '.' in fl:
#             if not os.path.exists(target_dir):
#                 os.mkdir(target_dir)  # создается целевая папка
#             try:
#                 shutil.copy(os.path.join(root, fl), os.path.join(target_dir, fl))
#             except Exception as e:
#                 print(f'File {fl} was not copied. {e}')