"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def person(name='Vasiliy', surname='Ivanov', birthday='1955',
           city='Moscow', email='vasil.the.best@vasil.ru', tel='+7999551155'):
    info = f'{name} {surname}, {birthday}, {city}, {email}, {tel}'
    return info


print(person())
