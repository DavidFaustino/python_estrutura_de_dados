matrix_a = [[0, 1], [2, 3]]
matrix_b = [[0, 1], [2, 3]]


# ordem da matrizes devem ser iguais
def addMatrix(ma, mb):
    lines_a = len(ma)
    columns_a = len(ma[0])
    lines_b = len(mb)
    columns_b = len(mb[0])

    if lines_a is lines_b and columns_a is columns_b:
        print('Addition')
        mc = [[0 for y in range(columns_a)] for x in range(lines_a)]
        for i in range(lines_a):
            for j in range(columns_a):
                mc[i][j] = ma[i][j] + mb[i][j]

        print(mc)
    else:
        print('Ordem das matrizes são diferentes!')


addMatrix(matrix_a, matrix_b)


def subMatrix(ma, mb):
    lines_a = len(ma)
    columns_a = len(ma[0])
    lines_b = len(mb)
    columns_b = len(mb[0])

    if lines_a is lines_b and columns_a is columns_b:
        print('Subtraction')
        mc = [[0 for y in range(columns_a)] for x in range(lines_a)]
        for i in range(lines_a):
            for j in range(columns_a):
                mc[i][j] = ma[i][j] - mb[i][j]
        print(mc)
    else:
        print('Ordem das matrizes são diferentes!')


subMatrix(matrix_a, matrix_b)


# a ordem de colunas da primeira matriz deve ser igual a ordem linhas da segunda matriz
def multMatrix(ma, mb):
    lines_a = len(ma)
    columns_a = len(ma[0])
    lines_b = len(mb)
    columns_b = len(mb[0])

    if columns_a is lines_b:
        print('Multiplication')
        mc = [[0 for y in range(lines_a)] for x in range(columns_b)]

        for i in range(lines_a):
            for y in range(columns_b):
                for x in range(lines_b):
                    mc[i][y] += ma[i][x] * mb[x][y]
        print(mc)
    else:
        print('Ordem da coluna da primeira matriz é diferente da ordem de linha da segunda matriz!')


matrix_a = [[0, 1, 2], [4, 5, 6]]
matrix_b = [[0, 1], [2, 3], [4, 5]]
multMatrix(matrix_a, matrix_b)




"""
Addition
[[0, 2], [4, 6]]
Subtraction
[[0, 0], [0, 0]]
Multiplication
[[10, 13], [34, 49]]
"""
