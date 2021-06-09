time = int(input('Введите время в секундах'))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time - (hours * 3600) - (minutes * 60)

print(f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}')
