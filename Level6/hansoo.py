def getNumber(num):
    arr = [0, 0, 0]
    i = 2
    while (num != 0):
        arr[i] = num % 10
        num //= 10
        i -= 1
    return arr


def checkHanSoo(arr):
    d = arr[1] - arr[0]
    if (arr[2] - arr[1] == d):
        return 1
    return 0


if __name__ == '__main__':
    num = int(input())
    cnt = 0
    if (num == 1000):
        num = 999
    elif (num < 100):
        cnt = num
    if (num >= 100):
        cnt = 99
        for i in range(100, num + 1):
            arr = getNumber(i)
            if (checkHanSoo(arr) == 1):
                cnt += 1
    print(cnt)
