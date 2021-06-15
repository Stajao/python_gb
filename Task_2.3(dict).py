months_dict = {
    ('12', '1', '2'): 'Зима',
    ('3', '4', '5'): 'Весна',
    ('6', '7', '8'): 'Лето',
    ('9', '10', '11'): 'Осень'
}
fl = True
check = [str(m) for m in range(1, 13)]

while fl:
    user_inp = input('Введите номер месяца: ')
    if user_inp in check:
        for i in months_dict.keys():
            if user_inp in i:
                print(months_dict[i])
                fl = False
    else:
        print('Неверный ввод')
