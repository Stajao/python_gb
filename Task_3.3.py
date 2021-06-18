"""
 Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func():
    arg1 = float(input('первый аргумент: '))
    arg2 = float(input('второй аргумент: '))
    arg3 = float(input('третий аргумент: '))
    lst = [arg1, arg2, arg3]
    max1 = max(lst)
    lst.remove(max1)
    max2 = max(lst)
    return f'Самые большие: {max1} и {max2}'


print(my_func())
