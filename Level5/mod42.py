arr = [0 for i in range(42)]
cnt = 0

for i in range(10):
    a = int(input())
    arr[a % 42] += 1
for i in range(len(arr)):
    if (arr[i] != 0):
        cnt += 1
print(cnt)
