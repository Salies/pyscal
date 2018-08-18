import math

size = 10 #change this to the ammount of lines you want to draw/calc
triangle = []

def factorial(x):
    if(x==0):
        return 1
    else:
        return math.factorial(x)

for n in range(size):
    triangle.append([])
    for p in range(n + 1):
        triangle[n].append([n, p])

def draw():
    for i in range(len(triangle)):
        for x in range(len(triangle[i])):
            print('%d ' % triangle[i][x][0], end=" ")
        print('')
        for y in range(len(triangle[i])):
            print('%s%d ' % ((" " * (len(str(triangle[i][x][0])) - len(str(triangle[i][y][1])))), triangle[i][y][1]), end=" ")
        print('\n')

def calc():
    for i in range(len(triangle)):
        for t in range(len(triangle[i])):
            print(int(factorial(triangle[i][t][0]) / (factorial(triangle[i][t][1]) * factorial(triangle[i][t][0] - triangle[i][t][1]))), end=" ") #n! / p!(n-p)!
        print('')

calc() #change to draw() for the binomials