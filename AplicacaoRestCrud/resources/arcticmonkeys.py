from flask_restful import Resource, reqparse

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

class HumbugSongs(Resource):
    def get(self):
        return {'Humbug Songs': humbug_songs}
    
class HumbugId(Resource):
    def get(self, humbug_id):
        for song in humbug_songs:
            if song['id'] == humbug_id:
                return song
        return {'message': 'Humbug song not found.'}, 404
       
    def post(self, humbug_id):
        args = reqparse.RequestParser()
        args.add_argument('title')
        args.add_argument('artist')
        args.add_argument('album')
        args.add_argument('release_date')
        args.add_argument('time')

        data_post = args.parse_args()

        new_song = {
            'id': humbug_id,
            'title': data_post['title'],
            'artist': data_post['artist'],
            'album': data_post['album'],
            'release_date': data_post['release_date'],
            'time': data_post['time']
        }

        humbug_songs.append(new_song)
        return new_song, 201

    def put(self, humbug_id):
        pass
    def delete(self, humbug_id):
        pass