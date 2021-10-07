
import string

alpha_upper = list(string.ascii_uppercase)

str = input()
result = list(0 for i in range(27))
for i in str:
    if(i >= 'a' and i <= 'z'):
        cnt = ord(i) - ord('a')
    else:
        cnt = ord(i) - ord('A')
    result[cnt] += 1


for i in range(result.index(max(result)) + 1,len(result)):
    if(result[i] == max(result)):
        print("?")
        quit()
print(alpha_upper[result.index(max(result))])
