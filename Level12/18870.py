def swapArr(arr2, rootIndex, childIndex):
    arr2[rootIndex], arr2[childIndex] = arr2[childIndex], arr2[rootIndex]


def heapsort(arr):
    for i in range(1, len(arr)):
        childIndex = i
        while(1):
            rootIndex = (childIndex - 1) // 2
            if(arr[rootIndex] < arr[childIndex]):
                swapArr(arr, rootIndex, childIndex)
            childIndex = rootIndex
            if(childIndex == 0):
                break
    for i in range(len(arr) - 1, -1, -1):
        swapArr(arr, 0, i)
        rootIndex = 0
        childIndex = 1
        while(rootIndex < i):
            childIndex = rootIndex * 2 + 1
            if(childIndex < i - 1 and arr[childIndex] < arr[childIndex + 1]):
                childIndex += 1
            if(childIndex < i and arr[rootIndex] < arr[childIndex]):
                swapArr(arr, rootIndex, childIndex)
            rootIndex = childIndex


def compressXY(arr, arr2):
    for i in range(len(arr)):
        for j in range(len(arr2)):
            if(arr[i] == arr2[j]):
                arr[i] = j
    for i in arr:
        print(i, end=' ')


num = int(input())
arr = list(map(int, input().split()))
arr2 = list(set(arr))
heapsort(arr2)
compressXY(arr, arr2)
