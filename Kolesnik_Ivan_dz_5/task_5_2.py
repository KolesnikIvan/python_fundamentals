n = int(input("Insert the upper bound of an odd number range: "))
odd_numbers = (i for i in range(1, n + 1) if i % 2)
print(*odd_numbers, sep=', ')
