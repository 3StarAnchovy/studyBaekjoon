def swapArr(arr):
    arr[0] , arr[1] = arr[1] , arr[0]

num = int(input())
arr = []
for i in range(num):
    arr.append(list(map(int, input().split(' '))))
for i in arr:
    swapArr(i)
arr.sort()
for i in arr:
    swapArr(i)
    print(i[0],i[1])

