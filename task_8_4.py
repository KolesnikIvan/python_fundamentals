"""Декоратор с аргументом-функцией (callback),
позволяющий валидировать входные значения функции
и выбрасывать исключение ValueError, если что-то не так"""

def val_checker(check_func):
    def _val_checker(func):
        def wrapper(arg):
            if not check_func(arg):
                raise ValueError('wrong wal ', arg)
            else:
                return func(arg)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5); print('1st a ', a)
a = calc_cube(-5); print('2nd a ', a)
