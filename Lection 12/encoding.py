#Урок 12. Кодировки

bytes_data = b'Some text that shoud be in binary format'
print(bytes_data[0]) #Вывод код символа первого элемента строки


#Кодировка
str_data_eng = 'Hello world!'
str_bytes = str_data_eng.encode('ascii')
print(str_bytes)

bytes_encoded = str_bytes
str_data_decoded = bytes_encoded.decode('ascii')
print(str_data_decoded)
