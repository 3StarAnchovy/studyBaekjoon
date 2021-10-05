a = 3
b = 3
array = []
while (a != 0 and b != 0):
    a,b = map(int, input().split(' '))
    array.append(a + b)
for i in range(len(array) - 1):
    print(array[i])