"""скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)"""

import os
import math

# folder = input('Insert path: ')
folder = '.'
result = dict()
for root, dirs, files in os.walk(folder):
    for fl in files:
        sz = os.stat(os.path.join(root, fl)).st_size
        idx = int(math.log10(sz) // 1)
        # раз ключи кратны десяти, они связаны с показателем степени 10; его и определяю
        if 10 ** idx in result:
            result[10 ** idx] +=  1
        else:
            result[10 ** idx] = 1
print(result, sep='\n')
