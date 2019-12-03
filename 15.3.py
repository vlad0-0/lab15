n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = 0
for i in range(n-1, -1, -1):
    if a[i]%2 == 1:
        b = a[i]
        break
for i in range(n):
    if a[i]%2 == 1:
        a[i] += b
print(a)
