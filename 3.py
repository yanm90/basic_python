class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return Cell(self.cell - other.cell)
        else:
            return "Разность ячеек меньше нуля"

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, rows):
        row = self.cell // rows
        more = self.cell % rows
        for i in range(row):
            print('*' * rows)
        print('*' * more)


cell_1 = Cell(13)
cell_2 = Cell(17)

print((cell_1 + cell_2).cell)
print((cell_2 - cell_1).cell)
print((cell_1 * cell_2).cell)
print((cell_2 / cell_1).cell)
cell_1.make_order(4)
