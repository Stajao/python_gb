"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

list1 = [[3, 5, 6, 1], [5, 6, 5], [9, 11, 24], [13, 24, 56]]
list2 = [[7, 3, 11], [3, 15, 6], [1]]


class Matrix:
    def __init__(self, list_of_lists):
        self.matr = list_of_lists

    def __fill_matr(self, mat1, mat2):
        if len(mat1) > len(mat2):
            for s in range(len(mat1) - len(mat2)):
                mat2.append([])
            for i in range(len(mat2)):
                if len(mat2[i]) < len(mat1[i]):
                    for y in range(len(mat1[i]) - len(mat2[i])):
                        mat2[i].append(0)
        elif len(mat1) > len(mat2):
            for s in range(len(mat2) - len(mat1)):
                mat1.append([])
            for i in range(len(mat1)):
                if len(mat1[i]) < len(mat2[i]):
                    for y in range(len(mat2[i]) - len(mat1[i])):
                        mat1[i].append(0)
        return mat1, mat2

    def __add__(self, other):
        result = []
        for row in range(len(self.__fill_matr(self.matr, other.matr)[0])):
            result.append(self.__fill_matr(self.matr, other.matr)[0][row])
            for i in range(len(self.__fill_matr(self.matr, other.matr)[0][row])):
                result[row][i] = self.__fill_matr(self.matr, other.matr)[0][row][i] + \
                                 self.__fill_matr(self.matr, other.matr)[1][row][i]
        return Matrix(result)

    def __str__(self):
        return '\n'.join('\t'.join(str(i) for i in row) for row in self.matr)


matrix1 = Matrix(list1)
matrix2 = Matrix(list2)

print(matrix1, '\n')
print(matrix2, '\n')

result = matrix1 + matrix2
print(result)
