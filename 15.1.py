n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())
a[:], b[:] = b[:], a[:]
print(*a)
print(*b)
