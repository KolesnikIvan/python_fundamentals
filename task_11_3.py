import time


class MyOwnTypeError(Exception):
    """Собственный класс-исключение проверяет
    содержимое списка на наличие только чисел."""
    def __init__(self, txt):
        self.text = txt


class MyOwnInterrupt(KeyboardInterrupt):
    def __init__(self):
        self.text = """Почему штатный KeyBoardInterrupt не работает с input()?
                    Пришлось привязаться к слову stop."""


num_lst = []
while True:
    try:
        new_val = input('Enter a value of list: ')
        if new_val == 'stop':
            raise MyOwnInterrupt
        elif not new_val.isnumeric():
            raise MyOwnTypeError('A value must be a number.')
    except MyOwnTypeError:
        pass
    # except KeyboardInterrupt as k:
    #     print(k)
    #     print(num_lst)
    #     break
    except MyOwnInterrupt as e:
        print(e)
        print(num_lst)
        break
    else:
        num_lst.append(new_val)
