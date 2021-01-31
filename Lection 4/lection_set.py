#Урок 4. Множества

faridun_things = {'Телефон', 'Книга', 'Мясо'}
kate_things = {'Телефон', 'Книга', 'Соль'}

#Общее
print(faridun_things | kate_things)
#Повторяющиеся
print(faridun_things & kate_things)
#Вещи которые есть у Фаридуна, но нет у Кейт
print(faridun_things - kate_things)
#Вещи которые есть у Кейт, но нет у Фаридуна
print(kate_things - faridun_things)
