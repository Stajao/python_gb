"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных о
наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class MyError(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    items = {}

    @staticmethod
    def inventory():
        result = []
        for key, value in Warehouse.items.items():
            if len(value) > 1:
                result.append([f'{key}s:', f"\n\tamount: {value[0]['amount']} \n\t Name: ",
                               '\n\t Name: '.join(', Serial Number: '.join([i for i in tpl]) for tpl in value[1:])])
        return '\n'.join(list(map(''.join, result)))

    @staticmethod
    def move_to_warehouse(*wares):
        for ware in wares:
            try:
                item = str(f'{ware.__class__}')[17:-2]
                if item not in Warehouse.items:
                    Warehouse.items[f'{item}'] = [{'amount': 0}]
                for i in Warehouse.items[f'{item}'][0:]:
                    if ware.sn in i:
                        raise MyError(f'Товар: {ware.sn} уже находится на складе')
            except MyError as err:
                print(err)
            else:
                if ware.location in InUse.depts:
                    InUse.items[ware.location].remove((ware.name, ware.sn))
                Warehouse.items[f'{item}'].append((ware.name, ware.sn))
                Warehouse.items[f'{item}'][0]['amount'] += 1
                ware.location = 'Warehouse'

    @staticmethod
    def move_in_use(dept, *wares):
        check_storage = []
        for value in Warehouse.items.values():
            for tpl in value:
                if type(tpl) == tuple:
                    for i in tpl:
                        check_storage.append(i)
        for ware in wares:
            try:
                item = str(f'{ware.__class__}')[17:-2]
                if ware.sn not in check_storage:
                    raise MyError(f'Товар {ware.sn} сначала надо принять на склад')
                if dept not in InUse.depts:
                    raise MyError(f'{dept}: такого отдела у нас нет')
                if dept not in InUse.items:
                    InUse.items[dept] = []
                for i in InUse.items[dept][0:]:
                    if ware.sn in i:
                        raise MyError(f'Товар: {ware.sn} уже выдан в этот отдел')
            except MyError as err:
                print(err)
            else:
                InUse.items[dept].append((ware.name, ware.sn))
                ware.location = dept
                Warehouse.items[f'{item}'].remove((ware.name, ware.sn))
                Warehouse.items[f'{item}'][0]['amount'] -= 1


class InUse(Warehouse):
    items = {}
    depts = ('Бухгалтерия', 'HR', 'IT')

    @staticmethod
    def inventory():
        result = []
        for key, value in InUse.items.items():
            if len(value) > 0:
                result.append([f'{key}: \n\t Name: ',
                               '\n\t Name: '.join(', Serial Number: '.join([i for i in tpl]) for tpl in value)])
        return '\n'.join(list(map(''.join, result)))


class OfficeEquipment:
    def __init__(self, name, sn, location=None):
        self.name = name
        self.sn = sn
        self.location = location

    @property
    def sn(self):
        return self.__sn

    @sn.setter
    def sn(self, sn):
        if len(sn) < 5:
            self.__sn = '{:{}{}{}}'.format(sn, '0', '>', 5).upper()
        elif len(sn) > 5:
            self.__sn = sn[0:5].upper()
        else:
            self.__sn = sn.upper()


class Printer(OfficeEquipment):
    def __init__(self, name, sn, print_type, location=None):
        super().__init__(name, sn, location)
        self.print_type = print_type


class Scanner(OfficeEquipment):
    def __init__(self, name, sn, scn_type, location=None):
        super().__init__(name, sn, location)
        self.scn_type = scn_type


class Multifunctional(Scanner, Printer):
    def __init__(self, name, sn, print_type, scn_type='floor', location=None):
        Scanner.__init__(self, name, sn, scn_type, location)
        Printer.__init__(self, name, sn, print_type)


test2 = Printer('Canon', 'ask2910885', 'laser')
test = Printer('HP', '2sa', 'laser')
test3 = Printer('Xerox', 'as23', 'laser')
scn1 = Scanner('MHP', 'sad22', 'table')
scn2 = Scanner('HP', 'p2om', 'floor')
mfu = Multifunctional('Vyatka', 'rui2', 'laser')
Warehouse.move_to_warehouse(test, test2)
Warehouse.move_to_warehouse(test2, test3, scn1)
Warehouse.move_to_warehouse(mfu)
print(Warehouse.inventory())
Warehouse.move_in_use('Бухгалтерия', test, scn1, scn1)
Warehouse.move_in_use('HR', scn2)
Warehouse.move_to_warehouse(scn1)
InUse.move_in_use('HR', test)
InUse.move_in_use('HR', mfu)
Warehouse.move_to_warehouse(scn2)
Warehouse.move_in_use('IT', scn2)
print(InUse.inventory())
