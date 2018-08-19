import math
from terminaltables import AsciiTable

size = 10 #change to the desired amount of lines (always remember that it starts with 0)
triangle = []

def factorial(x):
    if(x==0):
        return 1
    else:
        return math.factorial(x)

def count(n, p):
    return int(factorial(n) / (factorial(p) * factorial(n - p)))

def draw(x, y):
    return '%d\n%d' % (x, y)

def main(size, func):
    for n in range(size):
        triangle.append([])
        for p in range(n + 1):
            triangle[n].append(func(n,p))

main(size, count) #change to draw if you want the binomials

table = AsciiTable(triangle)
table.inner_heading_row_border = False
table.inner_row_border = True
print(table.table)