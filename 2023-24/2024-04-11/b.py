def r(s):
    n = len(s)
    if n % 2 == 0:
        s = s[: n // 2] + 'a' + s[n // 2 :]
    else:
        s = 'b' + s
    ans = ''
    for i in s:
        ans += alf[(alf.find(i) + 1) % 26]
    return ans

def r1(s):
    ans = ''
    for i in s:
        ans += alf[(alf.find(i) - 1) % 26]
    n = len(ans)
    if n % 2 == 0:
        return ans[1:]
    return ans[:n // 2] + ans[n // 2 + 1 :]
    
alf = 'abcdefghijklmnopqrstuvwxyz'

s = input()
v = int(input())
if v == 1:
    print(r(r(s)))
else:
    print(r1(r1(s)))