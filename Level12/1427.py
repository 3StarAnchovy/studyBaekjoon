num = int(input())
arr = []
while(num != 0):
    arr.append(num % 10)
    num = num // 10
arr = sorted(arr)
arr.reverse()
for i in arr:
    print(i, end='')
