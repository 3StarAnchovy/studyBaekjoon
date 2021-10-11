def getBalckJack(arr, max):
    Max = 0
    for i in range(0,len(arr) - 2):
        for j in range(i + 1,len(arr) - 1):
            for k in range(j + 1,len(arr)):
                if(arr[i] + arr[j] + arr[k] <= max and arr[i] + arr[j] + arr[k] > Max):
                    Max = arr[i] + arr[j] + arr[k]
    print(Max)

num, max = map(int, (input().split()))
arr = list(map(int, input().split()))
getBalckJack(arr, max)
