a = int(input())

for i in range(0, a):
    for j in range(i, a-1):
        print(' ', end='')
    for j in range(0, i+1):
        print('*', end='')
    print('')
