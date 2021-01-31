import json

users = [
    {
        'name': 'Faridun',
        'languages': ['Russian', 'Tajik', 'English'],
        'age': 18
    }    
]

with open('users.json', 'w') as f:
    json.dump(users, f)
