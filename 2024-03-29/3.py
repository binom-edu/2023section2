a=[int(i) for i in input().split()]
n=len(a)
for i in range(3):
   x=i
   for j in range(i+1, len(a)):
        if a[j] < a[x]:
            x = j
   a[i], a[x] = a[x], a[i]

print(*a)