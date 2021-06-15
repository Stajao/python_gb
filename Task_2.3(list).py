months = [('12', '1', '2'), ('3', '4', '5'), ('6', '7', '8'), ('9', '10', '11')]

while True:
    user_inp = input('Введите номер месяца (1-12): ')
    if user_inp in months[0]:
        print('Зима!')
    elif user_inp in months[1]:
        print('Весна!')
    elif user_inp in months[2]:
        print('Лето!')
    elif user_inp in months[3]:
        print('Осень!')
    else:
        print('Ввод неверный, попробуй снова')
        continue
    break
