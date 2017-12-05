vector = [1,2,3,4,5,6,7,8,9]

print(vector)

print('1 - Index')
sum = 0
for idx in range(len(vector)):
    element = vector[idx]
    print(element, end = ' ')
    sum += element
print()
print(sum)

print('2 - Element')
sum = 0
for element in vector:
    print(element, end= ' ')
    sum += element

print()
print(sum)


