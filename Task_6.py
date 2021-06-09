current = 7
target = 15
day = 1

print('Резултат:')
while current < target + 1:
    print(f'день {day} - результат: {current:.2f} км')
    current *= 1.1
    day += 1
print(f'На день {day} спортсмен достиг результата - не менее {target} км')
