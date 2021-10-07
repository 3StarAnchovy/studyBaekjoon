alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"
size = int(input())
for i in range(size):
    cnt, str = input().split()
    for i in str:
        print(i * int(cnt), end='')
    print()
