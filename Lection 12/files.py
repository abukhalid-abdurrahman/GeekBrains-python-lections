#Урок 12. Файлы


#Запись в файл
fout = open('sample.txt', 'w')
content = input('Input file content: ')
fout.writelines(content)
fout.close()

#Чтение из файла
fin = open('data.txt', 'r')
fileData = fin.readlines();
print(fileData)
fin.close()

#Автоматическое закрытие файла
with open('data.txt', 'r') as f:
    for line in f:
        print(line)
