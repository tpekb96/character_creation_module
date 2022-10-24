from math import sqrt
from inspect import cleandoc


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')

def CalculateSquareRoot (number):
    """Вычисляет квадратный корень"""
    return sqrt (number)

def calc (your_number):
    if your_number <= 0:
        return    
     
    root = 0
    print (cleandoc(f'Мы вычислили квадратный корень из введённого Вами числа.' 
           f' Это будет: {CalculateSquareRoot(your_number)}'))


print (cleandoc(message))
calc (25.5)
