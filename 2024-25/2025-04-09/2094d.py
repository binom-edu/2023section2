out = []
for _ in range(int(input())):
    p = input()
    s = input()
    if len(s) < len(p) or s[0] != p[0]:
        out.append('NO')
        continue
    pl = [1]
    sl = [1]
    cur = 1
    for i in range(1, len(p)):
        if p[i] == p[i - 1]:
            pl[-1] += 1
        else:
            pl.append(1)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            sl[-1] += 1
        else:
            sl.append(1)
    if len(pl) != len(sl):
        out.append('NO')
        continue
    for i in range(len(pl)):
        if not (pl[i] <= sl[i] <= 2 * pl[i]):
            out.append('NO')
            break
    else:
        out.append('YES')
for i in out:
    print(i)