matrix_2x2 = [[1, 2], [3, 4]]
print('1 - Matrix 2x2')
print(matrix_2x2)
print()

print('2 - Get by Index')
print(matrix_2x2[1][1])
print()

print('3 - Get by Range')
print(matrix_2x2[0:1])
print(matrix_2x2[1:2])
print(matrix_2x2[0:1][0][0])
print()

print('4 - Print All by Index')
for i in range(len(matrix_2x2)):
    for j in range(len(matrix_2x2[i])):
        print(matrix_2x2[i][j], end =' ')
    print()
print()

print('5 - Print All by Element')
for row in matrix_2x2:
    for element in row:
        print(element, end = ' ')
    print()
print()

print('6 - Join Elements')
for row in matrix_2x2:
    print(' '.join([str(element) for element in row]))

print()

print('7 - Sum by Index')
s = 0
for i in range(len(matrix_2x2)):
    for j in range(len(matrix_2x2[i])):
        s += matrix_2x2[i][j]
print(s)
print()

print('8 - Sum by Elements')
s = 0
for row in matrix_2x2:
    for element in row:
        s += element
print(s)
print()

"""
RESULT
1 - Matrix 2x2
[[1, 2], [3, 4]]

2 - Get by Index
4

3 - Get by Range
[[1, 2]]
[[3, 4]]
1

4 - Print All by Index
1 2 
3 4 

5 - Print All by Element
1 2 
3 4 

6 - Join Elements
1 2
3 4

7 - Sum by Index
10

8 - Sum by Elements
10

"""

