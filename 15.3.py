n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = 0
for i in range(n):
    if a[i]%2 == 1:
        if b == 0:
            b = a[i]
        elif b != 0:
            a[i] += b
            b = a[i]-b
print(a)
