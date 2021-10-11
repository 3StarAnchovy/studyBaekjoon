a,b = map(str, input().split())

reverse_a = 0
reverse_b = 0
for i in list(a[::-1]):
    reverse_a = 10 * reverse_a + int(i)
for i in list(b[::-1]):
    reverse_b = 10 * reverse_b + int(i)
if (reverse_a  > reverse_b):
    print(reverse_a)
else:
    print(reverse_b)