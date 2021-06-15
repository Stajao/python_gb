el = input('Введите элемент списка через пробел: ')
my_list = el.split()
print('Начальный список:', my_list)

search = 0
for i in my_list[::2]:
    number = my_list.index(i, search)
    if number + 1 < len(my_list):
        my_list[number], my_list[number + 1] = my_list[number + 1], my_list[number]
        search += 2
print('Измененный список:', my_list)
