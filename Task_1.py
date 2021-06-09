greeting = 'привет! я программа!'
nick_name = input('Введи ваш никнейм')
name = input('Введи ваше имя')
age = input('Введите ваш возраст')
city = input('Где вы живете?')

print(nick_name,', ',greeting, sep='')
print(f'Вас зовут {name}, вам {age} лет, и вы из города {city}!')
