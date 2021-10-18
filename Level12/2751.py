def heapSort(arr, num):
    # Min heap 생성
    for i in range(1, num):
        c = i
        while (1):
            rootIndex = (c - 1) // 2
            if (arr[rootIndex] > arr[c]):
                temp = arr[rootIndex]
                arr[rootIndex] = arr[c]
                arr[c] = temp
            c = rootIndex
            if (c == 0):
                break
    


num = int(input())
arr = []
for i in range(num):

    arr.append(int(input()))
heapSort(arr, num)