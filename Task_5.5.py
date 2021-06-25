"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open('5.5.txt', 'r+', encoding='UTF-8') as f:
    f.write(' '.join(map(str, [random.randint(1, 100) for i in range(random.randrange(0, 50))])))
    result = sum(map(int, f.read().split()))
print(result)
