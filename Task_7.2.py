"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def consumption_fabr(self):
        pass


class Coat(Clothes):
    def __init__(self, V, H=None):
        Clothes.__init__(self, V, H)

    def consumption_fabr(self):
        return round(self.V / 6.5 + 0.5, 2)

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V < 46:
            self.__V = 46
        elif V > 72:
            self.__V = 72
        else:
            self.__V = V


class Suit(Clothes):
    def __init__(self, H, V=None):
        Clothes.__init__(self, V, H)

    def consumption_fabr(self):
        return round(2 * self.H + 0.3, 2)

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        if H < 100:
            self.__H = 1
        elif H > 230:
            self.__H = 2.3
        else:
            self.__H = H / 100


coat1 = Coat(33)
print(coat1.V)
print(coat1.consumption_fabr())

suit1 = Suit(250)
print(suit1.H)
print(suit1.consumption_fabr())
