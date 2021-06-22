cube_lst = []
sum7 = 0  # сумма кратных семи
sum17 = 0  # сумма тех, у которых сумма цифр кратна семи
for i in range(1, 1000, 2):  # шагаем по нечетным
    curr_cube = i ** 3
    cube_lst.append(curr_cube)
    if curr_cube % 7 == 0:
        sum7 += curr_cube  # вычисляем сумму кубов, кратных семи

    curr_cube += 17  # увеличиваем куб на 17
    curr_cube_cp = curr_cube
    str_cube = str(curr_cube)
    sum_dgt = 0
    for j in range(len(str_cube)):  # считаем цифры в нем
        sum_dgt += curr_cube_cp % 10
        curr_cube_cp = curr_cube_cp // 10
    if sum_dgt % 7 == 0:
        sum17 += curr_cube
print(cube_lst, sum7, sum17, sep='\n')