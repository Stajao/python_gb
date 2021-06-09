number = int(input('Введите целое положительные число'))
biggest = -1

while number > 0:
    test = number % 10
    number = number // 10
    if test > biggest:
        biggest = test
print(biggest)
