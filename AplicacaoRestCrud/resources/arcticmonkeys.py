from flask import json
from flask_restful import Resource, reqparse
from models.arcticmonkeys import HumbugModel

class HumbugSongs(Resource):
    def get(self):
        return {'Humbug Songs': [song.json() for song in HumbugModel.query.all()]} # SELECT * FROM songs


class HumbugId(Resource):
    args = reqparse.RequestParser()
    args.add_argument('title', type=str, required=True, help="The field 'title' cannot be left blank.")
    args.add_argument('artist', type=str, required=True, help="The field 'artist' cannot be left blank.")
    args.add_argument('album', type=str, required=True, help="The field 'album' cannot be left blank.")
    args.add_argument('release_date', type=str, required=True, help="The field 'release_date' cannot be left blank.")
    args.add_argument('time', type=str, required=True, help="The field 'time' cannot be left blank.")

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
        try:
            new_song.save_song()
        except:
            return {'message': 'An internal error ocurred trying to save humbug song.'}, 500
        return new_song.json(), 201 # Created

    def put(self, humbug_id):
        data_put = HumbugId.args.parse_args()
        search_song = HumbugModel.find_song(humbug_id)
        if search_song:
            search_song.update_song(**data_put)
            search_song.save_song()
            return search_song.json(), 200
        
        new_song = HumbugModel(humbug_id, **data_put)
        try:
            new_song.save_song()
        except:
            return {'message': 'An internal error ocurred trying to save humbug song.'}, 500
        return new_song.json(), 201 # Created
    
    def delete(self, humbug_id):
        song = HumbugModel.find_song(humbug_id)
        if song:
            try:
                song.delete_song()
            except:
                return {'message': 'An internal error ocurred trying to delete humbug song.'}, 500    
            return {'message': 'Humbug song deleted.'}, 404
