expressions = ['15 * 3', '15 / 3', '15 // 2', '15 ** 2']
for expr in expressions:
    print(type(eval(expr)), end=', ')
