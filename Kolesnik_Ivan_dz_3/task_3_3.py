def thesaurus(*args):
    args_l = sorted(args)  # сортирую входной кортеж
    thes_dict = dict()  # объявляю словарь-результат
    for arg in args_l:
        if arg[0] not in thes_dict:
            # если буква ранее не встречалась, то записываем ее, как новый элемент словаря
            thes_dict[arg[0].title()] = [arg]
        else:
            # если буква уже была, добавляем к ее списку-значению еще элемент
            thes_dict[arg[0].title()].append(arg)
    return thes_dict


# print(thesaurus("Иван", "Мария", "Петр", "Илья"))
