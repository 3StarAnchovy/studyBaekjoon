def getNoMagic(num):
    result = num
    while(num != 0):
        result += num % 10
        num //= 10
    return result

if __name__ == '__main__':
    arr = set(range(1,10001))
    nomagic = set()
    for i in range(1,10001):
        nomagic.add(getNoMagic(i))
    magic = sorted(arr - nomagic)
    for i in magic:
        print(i)