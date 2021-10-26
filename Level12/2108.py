from collections import Counter

num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
arr = sorted(arr)

print(round(sum(arr)/num))  # 산술평균
print(arr[(num - 1) // 2])  # 중앙값

cnt = Counter(arr)
mode = cnt.most_common()

# 최빈값 # 여기 fix
if (len(mode) >= 2 and mode[0][1] == mode[1][1]):
    print(mode[1][0])
else:
    print(mode[0][0])

# 범위
print(abs(arr[0] - arr[-1]))
