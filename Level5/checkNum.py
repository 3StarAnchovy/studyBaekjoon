arr = [0 for i in range(10)]
a = int(input())
b = int(input())
c = int(input())
result = a*b*c
while (result != 0):
    arr[int(result % 10)] += 1
    result //= 10
for i in range(len(arr)):
    print(arr[i])