#Урок 4. Строки

developer = 'Faridun'
first_letter = developer[0]
end_letter = developer[-1]
range_letters = developer[1:4]
name_len = len(developer)
sub_string = developer.find('dun')

print('Первая буква имени разработчика: ', developer, ' = ', first_letter)
print('Последняя буква имени разработчика: ', developer, ' = ', end_letter)
print('Буквы в диапазоне от 1 до 4: ', range_letters)
print('Длина имени разрабочика(кол-во символов) ', name_len)
print('Поиск "dun" в имени разработчика(индекс): ', sub_string)

row_csv = 'Faridun;Berdiev;Hasanovich'
user_data = row_csv.split(';')
name_format = 'Имя:{}\nФамилия:{}\nОтчество:{}\n'.format(user_data[0].upper(), user_data[1].upper(), user_data[2].upper())
print(name_format)


