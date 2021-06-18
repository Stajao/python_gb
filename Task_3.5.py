"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_func(us_in):
    user_list = us_in.split(sep=' ')
    result_list = []
    flag = True
    for i in range(len(user_list)):
        if user_list[i] != '*':
            try:
                user_list[i] = float(user_list[i])
                result_list.append(user_list[i])
            except ValueError:
                print(f'Элемент {user_list[i]} был удален, т.к. не является числом')
        else:
            flag = False
            break
    return sum(result_list), flag


res = 0
while True:
    user_input = input('Введите числа через пробел и нажмите Enter, для завершения программы введите * ')
    extract = my_func(user_input)[:]
    res += extract[0]
    if extract[1]:
        print(res)
        continue
    else:
        break
print(res)
