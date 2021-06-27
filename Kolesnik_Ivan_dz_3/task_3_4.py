def thesaurus_adv(*args):
    args_s = sorted(args, key=lambda i: i.split(' ')[1][0])
    thes_dict = dict()
    for arg in args_s:
        fam_1st_letter = arg.split()[1][0].title()
        # объявляю первую букву фамилиии отдельной переменной,
        # а то каждый раз писать arg.split()[1][0] долго
        if fam_1st_letter in thes_dict:
            thes_dict[fam_1st_letter].append(arg)
        else:
            thes_dict[fam_1st_letter] = [arg]
    return thes_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
