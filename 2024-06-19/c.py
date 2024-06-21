out = []
for _ in range(int(input())):
    st = set()
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    pre = 0
    for i in range(n):
        if a[i] == pre:
            ans += 1
            st.add(a[i])
            pre += a[i]
        else:
            pre += a[i]
            if pre in st:
                ans += 1
            st.add(a[i])
    out.append(ans)

for i in out:
    print(i)