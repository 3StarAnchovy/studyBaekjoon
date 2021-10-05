a = int(input())
arr = []
for i in range(a):
    arr.append(input())
for i in range(len(arr)):
    cnt = 0
    score = 0
    for j in range(len(arr[i])):
        if (arr[i][j] == 'X'):
            cnt = 0
        else:
            cnt += 1
            score += cnt
    print(score)
