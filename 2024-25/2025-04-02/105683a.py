n = int(input())
a = [int(i) for i in input().split()] + [int(i) for i in input().split()]

print(sum(a) * 2 - max(a))