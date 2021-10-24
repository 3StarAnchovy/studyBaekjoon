def swapArr(arr, rootIndex, childIndex):
    temp = arr[rootIndex]
    arr[rootIndex] = arr[childIndex]
    arr[childIndex] = temp


def heapfify(arr, num):
    for i in range(1, num):
        childIndex = i
        while(1):
            rootIndex = (childIndex - 1) // 2
            if(arr[rootIndex] < arr[childIndex]):
                swapArr(arr, rootIndex, childIndex)
            childIndex = rootIndex
            if (childIndex == 0):
                break


def heapSort(arr, num):
    for i in range(num - 1, -1, -1):
        swapArr(arr, 0, i)
        rootIndex = 0
        childIndex = 1
        while(childIndex < i):
            childIndex = 2 * rootIndex + 1
            if (childIndex + 1 < i and arr[childIndex] < arr[childIndex + 1] ):
                childIndex += 1
            if (childIndex < i and arr[rootIndex] < arr[childIndex]):
                swapArr(arr, rootIndex, childIndex)
            rootIndex = childIndex
    

num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
heapfify(arr, num)
heapSort(arr, num)
for i in arr:
    print(i)
