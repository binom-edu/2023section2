def getUserInput():
    '''Ввод буквы с проверкой корректности'''
    while True:
        userInput = input('Введите букву: ').lower()
        if len(userInput) != 1:
            print('Требуется один символ')
            continue
        if userInput not in 'йцукенгшщзхъёфывапролджэячсмитьбю':
            print('Требуется русская буква')
            continue
        if userInput in wrong or userInput in correct:
            print('Такая буква уже называлась')
            continue
        return userInput

def makeDecission(letter):
    '''Принятие решения и обработка введенной буквы'''
    if letter in secret:
        print('Верно!')
        correct.append(letter)
    else:
        print('Ошибка!')
        wrong.append(letter)

def printFrame():
    '''Вывод состояния игры'''
    for i in secret:
        if i in correct:
            print(i, end=' ')
        else:
            print('-', end=' ')
    print()
    print('Ошибки:', *wrong)
    print(frames[len(wrong)])

def checkFinish():
    '''Проверка окончания игры'''
    if len(wrong) == len(frames) - 1:
        return -1
    for i in secret:
        if i not in correct:
            return 0
    return 1

frames = [
'''
-----||
  |  ||
     ||
     ||
     ||
     ||
========     
''',
'''
-----||
  |  ||
  o  ||
     ||
     ||
     ||
========     
''',
'''
-----||
  |  ||
  o  ||
  0  ||
     ||
     ||
========     
''',
'''
-----||
  |  ||
  o  ||
 /0  ||
     ||
     ||
========     
''',
'''
-----||
  |  ||
  o  ||
 /0\\ ||
     ||
     ||
========     
''',
'''
-----||
  |  ||
  o  ||
 /0\\ ||
 /   ||
     ||
========     
''',
'''
-----||
  |  ||
  o  ||
 /0\\ ||
 / \\ ||
     ||
========     
''',
]

with open('words.txt') as fin:
    words = fin.read().splitlines()

import random
secret = random.choice(words)
print(secret)

wrong = []
correct = []

gameOn = True
while gameOn:
    printFrame()
    letter = getUserInput()
    makeDecission(letter)
    result = checkFinish()
    if result == -1:
        print('К сожалению, вы проиграли! Было загадано слово:', secret)
        gameOn = False
    elif result == 1:
        print('Вы выиграли!')
        gameOn = False