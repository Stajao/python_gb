user_string = input('Введите строку ')
temp_list = user_string.split()

for number, i in enumerate(temp_list):
    print(f'{number+1} {i:.10}')
