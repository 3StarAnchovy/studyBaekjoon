def getFibonacci(num):
    if num == 0:
        return 0
    elif(num <= 2):
        return 1
    elif(num != 0):
        return (getFibonacci(num - 1) + getFibonacci(num - 2))
    

if __name__ == '__main__':
    num = int(input())
    print(getFibonacci(num))