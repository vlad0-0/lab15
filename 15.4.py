n = int(input())
a = []
a.append(int(input()))
maxel = a[0]
maxpos = 0
minel = a[0]
minpos = 0
for i in range(1, n):
    a.append(float(input()))
    if maxel < a[i]:
        maxel = a[i]
        maxpos = i
    if minel > a[i]:
        minel = a[i]
        minpos = i
if minpos > maxpos:
    minpos, maxpos = maxpos, minpos
for i in range(minpos, maxpos+1):
    a[i] = 0
print(a)
