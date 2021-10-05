a = int(input())
arr = []
for i in range(a):
    arr.append(list(map(int, input().split(' '))))
for i in range(a):
    cnt = 0
    avg = sum(arr[i][1:]) / (len(arr[i]) - 1)
    for j in range(1,len(arr[i])):
        if (arr[i][j] > avg):
            cnt += 1
    print('{:.3f}'.format(round((cnt / (len(arr[i]) - 1) * 100),3)),"%",sep = '')
