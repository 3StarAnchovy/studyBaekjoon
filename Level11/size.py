def sortSize(man):
    for i in man:
        for height in i[1]:
            
            for weight in i[0]:
                

num = int(input())
man = []
for i in range(num): #입력
    man.append(list(map(int,input().split())))
print(man)