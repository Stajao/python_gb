"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и
общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

result = {}
with open('subjects.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        t = line.rsplit()
        for i in range(1, len(t)):
            t[i] = (''.join(filter(lambda x: x.isdigit(), t[i])))
        result.update(dict.fromkeys([t[0]], sum(map(int, filter(None, t[1:]))))) #я не понимаю,
        # почему здесь fromkeys() берет слово из списка целиком, а в 5.7 перебирает по буквам
    print(result)
