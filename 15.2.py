n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
b = []
for i in range(1, n+1):
    b.append(sum(a[0:i])/i)
print(b)
