my_list = []
my_dict = {}
my_tuple = ()
user_input = None
temp_list = []
price_list = []
name_list = []
amount_list = []
unit_list = []
analitic = {}

while user_input != 4:
    user_input = int(input('Введите желаемую операцию (1-добавить товар в список, 2-показать текущий список товаров,' \
                           '3 вывести аналитику, 4-выход) '))
    if user_input == 1:
        name = input('Название товара: ')
        my_dict['Название'] = name
        price = int(input('Цена товара: '))
        my_dict['цена'] = price
        amount = int(input('Количество товара:'))
        my_dict['количество'] = amount
        unit = input('Единица измерения: ')
        my_dict['ед'] = unit
        temp_list.append(my_dict)
        for n, i in enumerate(temp_list):
            my_tuple = (n + 1, i)
        my_list.append(my_tuple)
        print(f'Описание вашего товара  выглядит так: {my_dict}')
        my_dict = {}
        continue
    elif user_input == 2:
        print(my_list)
    elif user_input == 4:
        continue
    elif user_input == 3:
        for i in range(len(my_list)):
            name_list.append(my_list[i][1].get('Название'))
            price_list.append(my_list[i][1].get('цена'))
            amount_list.append(my_list[i][1].get('количество'))
            if my_list[i][1].get('ед') not in unit_list:
                unit_list.append(my_list[i][1].get('ед'))
        analitic['Название'] = name_list
        analitic['цена'] = price_list
        analitic['количество'] = amount_list
        analitic['ед'] = unit_list
        print(analitic)
