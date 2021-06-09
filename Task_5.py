revenue = int(input('Укажите выручку вашей фирмы: '))
expenses = int(input('Укажите издержки вашей фирмы: '))

if revenue > expenses:
    print('Поздравляю, ваша фирма зарабатывает деньги!')
    profit = revenue - expenses
    print(f'Ваша прибыль составила: {profit} рублей, а рентабельность прибыли: {profit / revenue:.2f}')
    empl = int(input('Сколько сотрудников в вашей фирме? '))
    print(f'Прибыль на одного сотрудника составила: {profit / empl:.1f} рублей')
else:
    print('Вы банчите в минус, до свидания.')
