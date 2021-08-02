class MyOwnZeroDivisionException(Exception):
    """Собственный класс-исключение, обрабатывающий ситуацию деления на ноль."""
    pass


dividend = int(input("Input dividend: "))
divisor = int(input("Input divisor: "))

try:
    if divisor == 0:
        raise MyOwnZeroDivisionException('Divisor is incorrect')
except Exception as e:
    print(e)
else:
    print('Result: dividend / divisor = ', dividend / divisor)
finally:
    print('The end.')
