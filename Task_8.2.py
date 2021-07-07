"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyDivByZero(Exception):
    def __init__(self, text):
        self.text = text


try:
    a, b = float(input('Введите делимое: ')), float(input('Введите делитель: '))
    if b == 0:
        raise MyDivByZero('На ноль делить плохо')
except (ValueError, MyDivByZero) as err:
    print(err)
else:
    print(round(a / b), 3)
