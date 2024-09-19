for _ in range(int(input())):
    p = input()
    x, y = p[0], p[1]
    for i in '12345678':
        if i != y:
            print(x + i)
    for j in 'abcdefgh':
        if j != x:
            print(j + y)