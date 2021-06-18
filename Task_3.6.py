"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

letters = set('qwertyuiopasdfghjklzxcvbnm')


def int_func1(user_input):
    """удаляет слово целиком, если в нем есть недопустимые символы"""
    fl = True
    for i in user_input:
        if i in letters:
            fl = True
        else:
            fl = False
            break
    if fl == True:
        result = user_input.title()
        return result


def int_func2(user_input):
    """удаляет недопустимые символы из слова, составляет слово из остатков"""
    temp_result = []
    for i in range(len(user_input)):
        if user_input[i].lower() in letters:
            temp_result.append(user_input[i])
    result = ''.join(temp_result).title()
    return result


def res_func(my_func):
    us_in = input('Введите строку: ')
    temp_list = us_in.split(' ')
    final_list = []
    for i in temp_list:
        final_list.append(my_func(i))
    final_list = list(filter(None, final_list))
    res = ' '.join(final_list)
    return res


print(res_func(int_func1))
