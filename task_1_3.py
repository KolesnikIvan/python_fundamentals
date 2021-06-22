# склонние процентов
percent = int(input("Enter number "))
if percent <= 20:
    if percent == 1:
        print(percent, "процент")
    elif 2 <= percent <= 4:
        print(percent, "процента")
    else:
        print(percent, "процентов")
print('Wrong number; it must be less then 20.')
