"""Необходимо вывести те элементы списка, значения которых больше предыдущих"""
import sys
import time

start = time.perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = (nxt for nxt, prev in zip(src[1:], src) if nxt > prev)
# print(*(nxt for nxt, prev in zip(src[1:], src) if nxt > prev))
print(sys.getsizeof(res))
print(*res, sep=', ')
print('1st time: ', time.perf_counter() - start)


# альтернативный вариант с генераторной функцией
SRC = src
def alternative_variant():
    for num in SRC[1:]:
        if num > SRC[SRC.index(num) - 1]:
            yield num

start = time.perf_counter()
alt_gen = alternative_variant()
print(sys.getsizeof(alt_gen))
print(*alt_gen, sep=', ')
print('2nd time: ', time.perf_counter() - start)

# вывод: однострочный оказался медленнее, чем функция с yield


# еще одна альтернатива
start = time.perf_counter()
t_src = tuple(src)
res2 = (nxt for nxt, prev in zip(tuple(src[1:]), t_src) if nxt > prev)
# print(*(nxt for nxt, prev in zip(src[1:], src) if nxt > prev))
print(sys.getsizeof(res2))
print(*res2, sep=', ')
print('3rd time: ', time.perf_counter() - start)
# вывод: преобразование списка в кортеж помогло ускориться еще на треть
