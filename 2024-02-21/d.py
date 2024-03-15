for _ in range(int(input())):
    n, m = map(int, input().split())
    alf = 'vika'
    a = []
    for i in range(n):
        a.append(input())
    cnt = 0
    for j in range(m):    
        for i in range(n):
            if a[i][j] == alf[cnt]:
                cnt += 1
                break
        if cnt == 4:
            print('YES')
            break
    else:
        print('NO')