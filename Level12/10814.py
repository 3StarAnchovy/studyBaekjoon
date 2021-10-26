num = int(input())
arr = []
for i in range(num):
    arr.append(list(map(str, input().split())))
    arr[i][0] = int(arr[i][0])
arr.sort(key=lambda age: age[0])
for i in arr:
    print(i[0],i[1])
