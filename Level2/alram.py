def setAlram(hour, min):
    if min < 45:
        mod = 45 - min
        min = 60 - mod
        if (hour == 0):
            hour = 23
        else:
            hour -= 1
    else:
        min -= 45
    print(hour,min)


if __name__ == '__main__':
    hour, min = map(int, input().split(' '))
    setAlram(hour, min)
