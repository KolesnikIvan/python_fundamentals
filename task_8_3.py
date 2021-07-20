"""Декоратор для логирования типов позиционных аргументов функции.
Еесли аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции?"""

def type_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        # msg = tuple(*zip(args, map(type, args)))  #+ tuple(kwargs)
        # msg = (str(arg) + ':' + str(tp) for arg, tp in zip(args, map(type, args)))
        msg=list()  # решил записать явно
        for arg, tp in zip(args, map(type, args)):
            # условие создержит двоеточие; цикл, чтобы его вставить
            msg.append(str(arg) + ':' + str(tp))

        # такой же цикл для именованных аргументов
        for v, tp in zip(kwargs, map(type, kwargs.values())):
            msg.append(str(v) + ':' + str(tp))

        print(*msg, sep=', ')
        print('тип результата', type(result))
        print('выполнена ', func.__name__)

    return wrapper


@type_logger
def calc_cube(x, *args, **kwargs):
    return x ** 3

a = calc_cube(5, 8, 'ab', nm=1, str_s = 'abracadabra')