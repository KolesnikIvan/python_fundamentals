"""скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения —  — кортежи вида (<files_quantity>, [<files_extensions_list>])."""

import os
import math
import json

# folder = input('Insert path: ')
folder = '.'
result = dict()
for root, dirs, files in os.walk(folder):
    for fl in files:
        sz = os.stat(os.path.join(root, fl)).st_size
        idx = int(math.log10(sz) // 1)  # раз ключи кратны десяти, они связаны с показателем степени 10; его и определяю
        try:
            _, exp = fl.split('.')
            # print(fl, exp)
        except Exception as e:
            exp = 'no_expression'
        if 10 ** idx in result:
            num, tpl = result[10 ** idx]
            # tpl = list(tpl)
            num += 1
            if not exp in tpl:
                tpl.append(exp)
            result[10 ** idx] =  (num, tpl)
        else:
            result[10 ** idx] = (1, [exp])

print(result, sep='\n')

with open(os.path.join('.', 'result_dict'), 'w', encoding='utf-8') as f:
    json.dump(result, f)
