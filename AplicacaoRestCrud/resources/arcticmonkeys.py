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
        "id": 4,
        "title": "Secret Door",
        "artist": "Arctic Monkeys",
        "album": "Humbug",
        "release_date": "2009-08-19",
        "time": "3:43",

    }
]


class HumbugSongs(Resource):
    def get(self):
        return {'Humbug Songs': humbug_songs}


class HumbugId(Resource):
    args = reqparse.RequestParser()
    args.add_argument('title')
    args.add_argument('artist')
    args.add_argument('album')
    args.add_argument('release_date')
    args.add_argument('time')

    def find_song(humbug_id):
        for song in humbug_songs:
            if song['id'] == humbug_id:
                return song
        return None

    def get(self, humbug_id):
        song = HumbugId.find_song(humbug_id)
        if song:
            return song
        return {'Humbug Songs': None}, 404

    def post(self, humbug_id):

        data_post = HumbugId.args.parse_args()

        new_song = {
            'id': humbug_id,
            'title': data_post['title'],
            'artist': data_post['artist'],
            'album': data_post['album'],
            'release_date': data_post['release_date'],
            'time': data_post['time']
        }

        humbug_songs.append(new_song)
        return new_song, 200

    def put(self, humbug_id):
        data_put = HumbugId.args.parse_args()
        new_song = {'id': humbug_id, **data_put}
        song = HumbugId.find_song(humbug_id)
        if song:
            song.update(new_song)
            return new_song, 200

        humbug_songs.append(new_song)
        return new_song, 201

    def delete(self, humbug_id):
        global humbug_songs
        humbug_songs = [song for song in humbug_songs if song['id'] != humbug_id]
        return {'message': 'Humbug song deleted.'}
