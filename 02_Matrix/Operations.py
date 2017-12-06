matrix_a = [[0, 1], [2, 3]]
matrix_b = [[0, 1], [2, 3]]

matrix_c = [[0, 1, 2], [2, 3, 4]]


# ordem da matrizes devem ser iguais
def sumMatrix(ma, mb):
    lines_a = len(ma)
    columns_a = len(ma[0])
    lines_b = len(mb)
    columns_b = len(mb[0])

    if lines_a is lines_b and columns_a is columns_b:
        print('Soma')
        mc = [[0 for y in range(columns_a)] for x in range(lines_a)]
        for i in range(lines_a):
            for j in range(columns_a):
                mc[i][j] = ma[i][j] + mb[i][j]

        print(mc)
    else:
        print('Ordem das matrizes são diferentes!')


sumMatrix(matrix_a, matrix_b)


def subMatrix(ma, mb):
    lines_a = len(ma)
    columns_a = len(ma[0])
    lines_b = len(mb)
    columns_b = len(mb[0])

    if lines_a is lines_b and columns_a is columns_b:
        print('Subtração')
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
        print('Multiplicação')
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
Soma
[[0, 2], [4, 6]]
Subtração
[[0, 0], [0, 0]]
Multiplicação
[[10, 13], [34, 49]]
"""