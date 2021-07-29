import math

class Cell:
    """Класс «Клетка».

    Инициализируется количеством ячеек (целое число).
    Реализует перегрузку арифметических операторов.
    """
    def __init__(self, cell_number):
        self.cells = int(cell_number)

    def __add__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(self.cells + other.cells)
        else:
            raise ValueError('Оба слагаемых должны быть класса Cell')

    def __sub__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if self.cells > other.cells:
                return Cell(self.cells - other.cells)
            else:
                print("Substruction was not performed.")
                return self
        else:
            raise ValueError('Оба слагаемых должны быть класса Cell')

    def __mul__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if other.cells != 0:
                return Cell(self.cells * other.cells)
            else:
                print ('Multiplication was not performed.')
                return self
        else:
            raise ValueError('Оба сомоножителя должны быть класса Cell')

    def __floordiv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if other.cells != 0:
                return Cell(self.cells // other.cells)
            else:
                print('Division was not performed.')
                return self
        else:
            raise ValueError('Оба параметра должны быть класса Cell')

    # def division(self, other):
    #     if other.cells != 0:
    #         return Cell(round(self.cells / other.cells, 0))
    #     else:
    #         print('Division was not performed.')
    #         return self

    def __truediv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if other.cells != 0:
                return Cell(round(self.cells / other.cells, 0))
            else:
                print('Division was not performed.')
                return self
        else:
            raise ValueError('Оба параметра должны быть класса Cell')

    def __str__(self):
        return str(self.cells)

    def make_order(self, cells_in_line):
        n_lines = math.ceil(self.cells / cells_in_line)
        n_lines = int(self.cells / cells_in_line)
        order = ('*' * cells_in_line + '\n') * n_lines + '*' * (self.cells % cells_in_line) + '\n' * 2
        return order

c1 = Cell(9)
c2 = Cell(2)
c3 = Cell(3)

print(c1 + c2)
print(c1 - c2)
print(c1 / c2)
print(c1 / c3)
print(c1 // c2)
print(c1.make_order(2))
print(c1.make_order(3))
print(c1.make_order(5))
