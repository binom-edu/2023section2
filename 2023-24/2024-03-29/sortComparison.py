import random, time

# сравниваем алгоритмы сортировок

def quickSort(lst, l, r):
    if l >= r:
        return
    x = lst[random.randint(l, r)]
    i = l
    j = r
    while i <= j:
        while i < r and lst[i] < x:
            i += 1
        while j > l and lst[j] > x:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    quickSort(lst, l, j)
    quickSort(lst, i, r)

def selectionSort(lst):
    for i in range(n - 1):
        idx = i
        for j in range(i, n):
            if lst[j] < lst[idx]:
                idx = j
        lst[i], lst[idx] = lst[idx], lst[i]

def bubbleSort(lst):
    for i in range(n):
        for j in range(n - 1, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]

def isSorted(lst):
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

n = 10 ** 5
a = [random.randint(-100, 100) for i in range(n)]
lst1 = a.copy()
lst2 = a.copy()
lst3 = a.copy()

start = time.time()
quickSort(lst1, 0, n - 1)
stop = time.time()
print('Быстрая сортировка')
if isSorted(lst1):
    print(stop - start)
else:
    print('Fail')

start = time.time()
selectionSort(lst2)
stop = time.time()
print('Сортировка выбором')
if isSorted(lst2):
    print(stop - start)
else:
    print('Fail')

start = time.time()
bubbleSort(lst3)
stop = time.time()
print('Пузырьковая сортировка')
if isSorted(lst3):
    print(stop - start)
else:
    print('Fail')