my_list = [True, None, 'string', 123, 39.4, b'0123', (10 + 98j), ('a', 'b', 10), {'a': 10, 'b': 20}, {'a', 'b', 12},
           ['k', 's', 10], bytearray(123)]
for number, i in enumerate(my_list):
    print(f'Элемент списка под индексом {number} имеет тип {str(type(i))[8:-2]}')
