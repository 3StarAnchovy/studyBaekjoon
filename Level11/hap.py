def checkBoon(num):
    pre = num
    result = 0
    while (num != 0):
        result += num % 10
        num //= 10
    return result + pre

num = int(input())
i = 0
while(checkBoon(i) != num):
    i += 1
    if ( i>num):
        print(0)
        quit()
print(i)