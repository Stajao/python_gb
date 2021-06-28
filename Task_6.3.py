"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""
spirit_coach = {'wage': 10000, 'bonus': 5000}


class Worker:
    def __init__(self, name, surname, position, salary_dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = salary_dict


class Position(Worker):
    def __init__(self, name, surname, position, salary_dict):
        super().__init__(name, surname, position, salary_dict)

    def get_full_name(self):
        print(f'Имя: {self.name}, Фамилия: {self.surname}')

    def get_total_income(self):
        print('Зарплата с учетом бонуса: {0} рублей'.format(self._income['wage'] + self._income['bonus']))


inokkentiy = Position('Иннокентий', 'Шмидт', 'Духовный коуч', spirit_coach)
inokkentiy.get_full_name()
inokkentiy.get_total_income()
