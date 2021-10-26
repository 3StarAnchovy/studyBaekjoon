num = int(input())
arr = []
for i in range(num):
    arr.append(input())
arr = list(set(arr))  # 중복제거
arr.sort()  # 알파벳순 정렬
arr.sort(key = len)  # 길이별 정렬
for word in arr:
    print(word)
