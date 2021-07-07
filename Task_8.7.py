"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplNumber:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __str__(self):
        return f'({self.Re}+{self.Im}j)' if self.Im >= 0 else f'({self.Re}{self.Im}j)'

    def __add__(self, other):
        return ComplNumber(self.Re + other.Re, self.Im + other.Im)

    def __mul__(self, other):
        return ComplNumber((self.Re * other.Re) - (self.Im * other.Im), (self.Re * other.Im + other.Re * self.Im))


my_number1 = ComplNumber(3, 5)
my_number2 = ComplNumber(4, -1)
print((3 + 5j) + (4 - 1j))
print(my_number1 + my_number2)
print((3 + 5j) * (4 - 1j))
print(my_number1 * my_number2)

print((3 + 5j) * (complex(str(my_number2))))
