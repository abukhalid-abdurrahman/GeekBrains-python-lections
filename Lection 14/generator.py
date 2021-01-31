#Урок 14. Генераторы

numbers = [5, 3, 1, 3, 4, 1, 3, 4, 5, 201]


#Использование генератора для заполнения списка
result = [number for number in numbers if number > 4]

print('Result: ', result)
