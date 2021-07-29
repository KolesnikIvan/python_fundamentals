class Matrix:
    """Класс Matrix (матрица) принимает список списков для формирования матрицы"""
    def __init__(self, elements):
        self._elements = elements
        self.m = len(elements)
        self.n = len(list(elements[0]))

    def __str__(self):
        """Перегрузку метода __str__() для вывода матрицы в привычном виде.

        Returns formatted multiline string.
        """
        # return '\n'.join('\t'.join(elements[i][j] for i in range(self.m) for j in range(self.n)
        return '\n'.join('\t'.join(str(self._elements[j][i]) for i in range(self.n)) for j in range(self.m))

    def elements(self):
        # выношу elements в public (НЕprotected) метод,
        # чтоб перегруженный __add__ не подчеркивал other.elements()
        # в свойство не стал превращать, т.к. использую только один раз
        return self._elements

    def __add__(self, other):
        """Перегрузка метода __add__() для  сложения двух объектов класса Matrix.

         Результатом сложения должна быть новая матрица.
         Сложение элементов матриц выполняется поэлементно.
         Первый элемент первой строки первой матрицы
         складываем
         с первым элементом первой строки второй матрицы и пр.

        """
        mx_sum = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                mx_sum[i][j] = self._elements[i][j] + other.elements()[i][j]
        return Matrix(mx_sum)

mx1 = Matrix([[31, 22], [37, 43], [51, 86]])
mx2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
mx3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(mx1)
print(mx2)
print(mx3)
print(mx1 + mx1)
