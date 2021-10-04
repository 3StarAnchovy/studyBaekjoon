num = int(input())
array = []
for i in range(0, num):
    a, b = map(int, input().split(' '))
    array.append(a+b)

for i in range(0, num):
    print("Case #",i, ": ", array[i],sep='')
