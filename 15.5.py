n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
while a[1:n+1] != sorted(a[1:n+1]):
    print("Массив [1:"+str(n)+"] не отсортирован, введите заново")
    for i in range(1, n):
        a[i] = float(input())
l = 1
r = n-1
while r-l > 1:
    if a[(l+r)//2] > a[0]:
        r = (l+r)//2
    elif a[(l+r)//2] < a[0]:
        l = (l+r)//2
    else:
        break
a.insert((l+r)//2, a.pop(0))
print(a)
