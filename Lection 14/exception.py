#Урок 14. Исключения

ownerName = input('Input Name: ')

if ownerName != 'Faridun':
    raise Exception('Owner Name must be Faridun!')

print('Successfulley authorized!')
