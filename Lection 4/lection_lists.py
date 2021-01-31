#Урок 4. Списки

names_list = ['Faridun', 'Kamila', 'Nisso', 'Ramz']
variable_type = type(names_list)
result_format = 'Тип объекта: {}'.format(variable_type)
list_len = len(names_list)


print(result_format)
print('Длинна списка: ', list_len)

#Добавление элемента в список
names_list.append('Kalabok')
list_len = len(names_list)
print('Длинна списка после добавление элемента: ', list_len)

#Удаление элемента из списка
first_deleted_el = names_list.pop()
removed_el = names_list.remove('Faridun')
del names_list[0]
print('Удаленный элемент: ', first_deleted_el)

list_len = len(names_list)
print('Данные: ', names_list)
print('Длинна списка: ', list_len)

#Проверки/Поиск в списке
if 'Nisso' in names_list:
    print('Элемент Nisso содержится в списке')
elif 'Kamila' in names_list:
    print('Элемент Kamila содержится в списке')
