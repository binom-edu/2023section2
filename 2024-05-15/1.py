s = 'abcdefgh'
# s[1] = 'B'
# print(s)
s = s[:1] + 'B' + s[2:] #конкатенация
print(s)
for i in s:
    print(i)