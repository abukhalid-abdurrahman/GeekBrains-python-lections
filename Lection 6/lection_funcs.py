#Урок 8. Функции

def setUsersParams(**params):
    for k, v in params.items():
        print('User Param: {}: {}'.format(k, v))

def createUsers(*userNames):
    print('Creating users: ', userNames)

setUsersParams(age='18', alive='true')
createUsers('Kate', 'Max', 'Leo')


#Лямбда функции


def filterNumbers(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

data = filterNumbers([10, 3, 4, 1, 4, 1, 4],
              lambda number: number > 3);

print(data)


