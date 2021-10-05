num = int(input())
arr = []
arr = list(map(int, input().split(' ')))
MAX = max(arr)
for i in range(num):
    arr[i] = arr[i] / MAX * 100
avg = sum(arr) / num
print(avg)