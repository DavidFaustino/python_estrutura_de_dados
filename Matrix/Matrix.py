matrix_2x2 = [[1, 2], [3, 4]]
print(matrix_2x2)

print()

print('1 - Index')
for i in range(len(matrix_2x2)):
    for j in range(len(matrix_2x2[i])):
        print(matrix_2x2[i][j], end =' ')
    print()


print('2 - Row')
for row in matrix_2x2:
    for element in row:
        print(element, end = ' ')
    print()

print('3 - Join Elements')
for row in matrix_2x2:
    print(' '.join([str(element) for element in row]))

print('4 - Sum elements')
s = 0
for i in range(len(matrix_2x2)):
    for j in range(len(matrix_2x2[i])):
        s += matrix_2x2[i][j]
print(s)

print('5 - Sum elements')
s = 0
for row in matrix_2x2:
    for element in row:
        s += element
print(s)


