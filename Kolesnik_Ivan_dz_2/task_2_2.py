raw_msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(raw_msg))
for i in range(len(raw_msg)):
    if raw_msg[i].isnumeric():
        n = int(raw_msg[i])  # если элемент списка можно просто преобразовать, то делаю это
        raw_msg[i] = f'{n:02d}'
        # print(raw_msg)
    else:
        n = ''  # эта ветка условия нацелена на +5
        for l in raw_msg[i]:  # не понял, почему здесь warning ambiguous variable name 'l'
            # if 0 <= int(l) <= 9:
            if 48 <= ord(l) <= 57:  # извлекаю символы цифры по их кодам
                n += l  # извлекаю цифры
        if n != '':
            raw_msg[i] = raw_msg[i][:raw_msg[i].index(n[0])]  # извлекаю нецифровые символы
            n2 = int(n)
            n3 = f'{n2:02d}'
            raw_msg[i] += n3  # соединяю нецифры и цифры
            # print(raw_msg)
print(' '.join(raw_msg))
print(id(raw_msg))
