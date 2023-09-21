from flask import json
from flask_restful import Resource, reqparse
from models.arcticmonkeys import HumbugModel

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

    def get(self, humbug_id):
        song = HumbugModel.find_song(humbug_id)
        if song:
            return song.json()
        return {'Humbug Songs': None}, 404

    def post(self, humbug_id):
        if HumbugModel.find_song(humbug_id):
            return {"message": f"Humbug song id {humbug_id} already exists."}, 400 # Bad Request
        data_post = HumbugId.args.parse_args()
        new_song = HumbugModel(humbug_id, **data_post)
        new_song.save_song()
        return new_song.json(), 201 # Created

    def put(self, humbug_id):
        data_put = HumbugId.args.parse_args()
        new_song = HumbugModel(humbug_id, **data_put).json()
        song = HumbugModel.find_song(humbug_id)
        if song:
            song.update(new_song)
            return new_song, 200

        humbug_songs.append(new_song)
        return new_song, 201
    
    def delete(self, humbug_id):
        global humbug_songs
        humbug_songs = [song for song in humbug_songs if song['id'] != humbug_id]
        return {'message': 'Humbug song deleted.'}
