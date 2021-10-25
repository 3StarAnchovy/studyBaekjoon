def swapArr(arr, rootIndex, childIndex):
    temp = arr[rootIndex]
    arr[rootIndex] = arr[childIndex]
    arr[childIndex] = temp

#MaxHeap 생성
def heapify(num, arr):
    for i in range(1, num):
        childIndex = i
        rootIndex = 1
        while(rootIndex != 0):
            rootIndex = (childIndex - 1) // 2
            if(arr[rootIndex] < arr[childIndex]):
                swapArr(arr, rootIndex, childIndex)
            childIndex = rootIndex

#크기를 한개씩 줄여가며 정렬
#Heap 구조이므로 맨 앞에 값은 최대값임 -> 최대값을 맨 뒤로 보냄
#난 천재야 역시
def heapSort(num, arr):
    for i in range(num - 1, -1, -1):
        swapArr(arr,0,i)
        rootIndex = 0
        childIndex = 1
        while (childIndex < i):
            childIndex = rootIndex * 2 + 1
            if(childIndex + 1 < i and arr[childIndex] < arr[childIndex + 1]):
                childIndex += 1
            if(childIndex < i and arr[childIndex] > arr[rootIndex]):
                swapArr(arr,childIndex,rootIndex)
            rootIndex = childIndex
    print(arr)

num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
heapify(num, arr)
heapSort(num, arr)
