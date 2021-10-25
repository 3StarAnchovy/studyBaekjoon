def countingSort(num,arr,cnt):
    print()
    for i in range(num):
        cnt[arr[i] - 1] += 1
    for i in range(num):
        if(cnt[i] != 0):
            for j in range(cnt[i]):
                print(i + 1)

num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
cnt = [0 for i in range(1000)]
countingSort(num,arr,cnt)