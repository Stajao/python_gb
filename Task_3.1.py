"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def dev():
    try:
        a = int(input('делимое:'))
        b = int(input('делитель '))
        res = a / b
    except ValueError:
        return 'вводи циферки'
    except ZeroDivisionError as err:
        return err
    return res


print(dev())
