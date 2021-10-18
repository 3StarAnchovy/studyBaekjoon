def swapArray(a,b,arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def heapfify(num, arr):
    for i in range(1, num):
        childIndex = i
        while(1):
            rootIndex = (childIndex - 1) // 2
            if(arr[rootIndex] < arr[childIndex]):
                swapArray(rootIndex,childIndex,arr)
            childIndex = rootIndex
            if (childIndex == 0):
                break
    print(arr)


num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
heapfify(num, arr)
