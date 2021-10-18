def heapSort(arr, num):
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
    rst = arr[0]
    arr.remove(rst)
    return (rst)


num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
for i in range(num):
    print(heapSort(arr, num))
    num -= 1
