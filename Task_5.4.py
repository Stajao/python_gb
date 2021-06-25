"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('russian.txt', 'w', encoding='UTF') as result:
    with open('english.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        for key in russian.keys():
            text = text.replace(key, russian[key])
    result.write(text)
