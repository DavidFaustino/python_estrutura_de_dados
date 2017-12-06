vector = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('1 - Vector')
print(vector)
print()

print('2 - Get by Index')
print(vector[2])
print()

print('3 - Get by Range')
# o último elemento é um limite superior aberto
print(vector[2:5])
print(vector[:5])
# todos elementos do vetor
print(vector[:])
print()

print('4 - Print All by Index')
for idx in range(len(vector)):
    element = vector[idx]
    print(element, end=' ')
print()
print()

print('5 - Print All by Element')
for element in vector:
    print(element, end=' ')
print()
print()

print('6 - Sum All by Index')
sum = 0
for idx in range(len(vector)):
    sum += vector[idx]
print(sum)
print()

print('7 - Sum All by Element')
sum = 0
for element in vector:
    sum += element
print(sum)
print()

"""
RESULT
1 - Vector
[1, 2, 3, 4, 5, 6, 7, 8, 9]

2 - Get by Index
3

3 - Get by Range
[3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

4 - Print All by Index
1 2 3 4 5 6 7 8 9

5 - Print All by Element
1 2 3 4 5 6 7 8 9 

6 - Sum All by Index
45

7 - Sum All by Element
45
"""
