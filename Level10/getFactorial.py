def getFactorial(num):
    if (num != 0):
        return num * getFactorial(num - 1)
    return 1


if __name__ == '__main__':
    num = int(input())
    print(getFactorial(num))
