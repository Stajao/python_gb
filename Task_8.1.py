"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import re


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_convert(cls, date_inp):
        try:
            dd, mm, yyyy = map(int, re.split('[., /:;]', date_inp))
            if not cls.validate(dd, mm, yyyy):
                raise MyError('Такой даты не бывает')
        except (ValueError, MyError) as err:
            print(err)
        else:
            return cls(dd, mm, yyyy)

    @staticmethod
    def validate(_dd, _mm, _yyyy):
        return True if 31 <= _dd > 0 < _yyyy <= 9999 and 0 < _mm <= 12 else False


date1 = Date.date_convert('31;12/2020')
print(date1.day, date1.month, date1.year)
date2 = Date.date_convert('32.34.2444')
