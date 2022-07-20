# 1. Вычислить результат деления двух чисел c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal

def cheking(num1, num2, acc):
    while True:
        try:
            num1 = Decimal(num1)
            break
        except:
            print('Вы ввели не число')
            num1 = input('Введите первое число: ')
    while True:
        try:
            num2 = Decimal(num2)
            if num2 == 0:
                print('Делить на ноль нельзя')
                num2 = input('Введите второе число: ')
            else:
                break
        except:
            print('Вы ввели не число')
            num2 = input('Введите второе число: ')
    while True:
        try:
            acc = Decimal(acc)
            break
        except:
            print('Вы ввели не число')
            acc = input('Введите точность в виде числа: ')
    return num1, num2, str(acc)


a = input('Введите первое число: ')
b = input('Введите второе число: ')
d = input('Введите точность, например, "0.001" или "10е-3": ')
x, y, z = cheking(a, b, d)
print(f'{x} / {y} = {(x / y).quantize(Decimal(z))}')

