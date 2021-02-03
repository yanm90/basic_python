class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        output = ""
        for i in self.matrix:
            for ii in i:
                output += str(ii) + '\t'
            output += '\n'
        return output

    def __add__(self, other):
        try:
            for i in range(len(self.matrix)):
                for ii in range(len(self.matrix[i])):
                    self.matrix[i][ii] += other.matrix[i][ii]
            return Matrix(self.matrix)
        except IndexError:
            return 'Ошибка. Матрицы суммируются только равноразмерные'


mx1 = Matrix([[4, 9], [5, 1], [3, 6]])
mx2 = Matrix([[6, 1], [5, 9], [7, 3]])
print(mx1 + mx2)
