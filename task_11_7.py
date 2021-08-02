import math
import random


class ComplexNumber:
    """Класс «Комплексное число».
    Реализует перегрузку методов сложения и умножения комплексных чисел."""
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imag = imaginary_part

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)

    def __mul__(self, other):
        re = self.real * other.real - self.imag * other.imag
        im = self.real * other.imag + other.real * self.imag
        return ComplexNumber(re, im)

    def __str__(self):
        return str(self.real) + "+" + str(self.imag) + "*i"


# проверка работы, сопоставление со встроенным механизмом работы с комплесными числами
for i in range(8):
    r1 = random.random() * 10
    i1 = random.random() * 10
    r2 = random.randint(0, 10)
    i2 = random.randint(0, 10)
    c1 = ComplexNumber(r1, i1)
    c2 = ComplexNumber(r2, i2)
    cs1 = complex(r1, i1)
    cs2 = complex(r2, i2)
    print("c1 =", c1, ", c2 =", c2)
    print('c1+c2=', c1 + c2)
    print('cs1+cs2=', cs1 + cs2)
    print('c1*c2=', c1 * c2)
    print('cs1*cs2=', cs1 * cs2)
    print('abs my own class', abs(c1), '\n',
          'abs built-in class', abs(cs1))
    # input()
