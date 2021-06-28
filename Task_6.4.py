"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}' if direction in ('налево', 'направо') else f'{self.name} поехала '
                                                                                              f'в неизвестном направлении')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'{self.name} едет со скоростью {self.speed} км/ч' if self.speed <= 60 else f'{self.name} едет слишком быстро!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'{self.name} едет со скоростью {self.speed} км/ч' if self.speed <= 60 else f'{self.name} едет слишком быстро!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


pc1 = PoliceCar(100, 'blue', 'VW', True)
tc1 = TownCar(80, 'red', 'Lada', False)
sc1 = SportCar(300, 'green', 'Porsche', False)
wc1 = WorkCar(30, 'yellow', 'KAMAZ', False)

print(pc1.name, tc1.name, wc1.name)
print(pc1.speed)

tc1.show_speed()
tc1.stop()
wc1.go()
wc1.turn('налево')
wc1.stop()
tc1.go()
sc1.turn('выфаы')
