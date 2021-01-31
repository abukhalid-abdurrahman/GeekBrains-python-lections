import random

sys_number = random.randint(1, 100)
count = 0
max_count = 5

while True:
    count += 1
    user_number = int(input('Введите число: '))

    if count >= max_count:
        print('Вы проиграли!')
        break
    
    if sys_number == user_number:
        print('Победа за ', count, ' попыток!')
        break
    elif sys_number < user_number:
        print('Ваше число больше загадонного!')
    elif sys_number > user_number:
        print('Ваше число меньше загадонного!')
