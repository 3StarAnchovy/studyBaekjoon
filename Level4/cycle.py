num = int(input())
cnt = 0
new = num
while (1):
    ten = int(new / 10)
    one = new % 10
    result = ten + one;
    new = one * 10 + result % 10
    cnt += 1
    if (new == num):
        break
print(cnt)
