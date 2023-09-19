from flask_restful import Resource

humbug_songs = [
    {
        'id': 1,
        'title': 'My Propeller',
        'artist': 'Arctic Monkeys',
        'album': 'Humbug',
        'release_date': '2009-08-19',
        'time': '3:27',
        
    },
    {
        'id': 2,
        'title': 'Crying Lightning',
        'artist': 'Arctic Monkeys',
        'album': 'Humbug',
        'release_date': '2009-08-19',
        'time': '3:45',
        
    },
    {
        'id': 3,
        'title': 'Dangerous Animals',
        'artist': 'Arctic Monkeys',
        'album': 'Humbug',
        'release_date': '2009-08-19',
        'time': '3:30',
        

    }, 
    {
        'id': 4,
        'title': 'Secret Door',
        'artist': 'Arctic Monkeys',
        'album': 'Humbug',
        'release_date': '2009-08-19',
        'time': '3:43',
        
    }
]

class Humbug(Resource):
    def get(self):
        return {'Humbug Songs': humbug_songs}