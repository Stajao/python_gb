rating = [8, 7, 5, 5, 5, 2, 1]
user_number = None

while user_number != 'stop':
    user_number = input(f'Текущий рейтинг: {rating}\nВведите новый элемент в рейтинге или введите stop для остановки: ')
    if user_number.isdigit():
        user_number = int(user_number)
        for i in range(len(rating)):
            if user_number >= rating[i]:
                rating.insert(i, user_number)
                break
            elif rating[i] > user_number > rating[i + 1]:
                rating.insert(i + 1, user_number)
                break
            elif user_number < rating[-1]:
                rating.append(i)
                break
    elif user_number == 'stop':
        continue
    else:
        print('Неверный ввод')
print(rating)
