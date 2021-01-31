import pickle

game_objects = [
    {
        'name': 'player',
        'objectId': 998123,
        'guid': '2b86c4a9-ba6f-4bc4-aaf0-66e4744fded2',
        'position': {
            'x': 0,
            'y': 10
        }
    }
]

with open('data.txt', 'wb') as f:
    pickle.dump(game_objects, f)

with open('data.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)
