from flask import json
from flask_restful import Resource, reqparse
from models.suckitandsee import SuckItAndSeeModel
from flask_jwt_extended import jwt_required
from flask import request


class SuckItAndSeeSongs(Resource):
    def get(self):

        title_filter = request.args.get('title')
        artist_filter = request.args.get('artist')
        album_filter = request.args.get('album')
        release_date_filter = request.args.get('release_date')
        time_filter = request.args.get('time')
        
        songs = SuckItAndSeeModel.query

        if title_filter:
            songs = songs.filter_by(title=title_filter)
        if artist_filter:
            songs = songs.filter_by(artist=artist_filter)
        if album_filter:
            songs = songs.filter_by(album=album_filter)
        if release_date_filter:
            songs = songs.filter_by(release_date=release_date_filter)
        if time_filter:
            songs = songs.filter_by(time=time_filter)

        return {'Suck It And See Songs': [song.json() for song in songs.all()]}


class SuckItAndSeeId(Resource):
    args = reqparse.RequestParser()
    args.add_argument('title', type=str, required=True,
                      help="The field 'title' cannot be left blank.")
    args.add_argument('artist', type=str, required=True,
                      help="The field 'artist' cannot be left blank.")
    args.add_argument('album', type=str, required=True,
                      help="The field 'album' cannot be left blank.")
    args.add_argument('release_date', type=str, required=True,
                      help="The field 'release_date' cannot be left blank.")
    args.add_argument('time', type=str, required=True,
                      help="The field 'time' cannot be left blank.")

    def get(self, suckitandsee_id):
        song = SuckItAndSeeModel.find_song(suckitandsee_id)
        if song:
            return song.json()
        return {'Suck It And See Songs': None}, 404

    @jwt_required()
    def post(self, suckitandsee_id):
        if SuckItAndSeeModel.find_song(suckitandsee_id):
            # Bad Request
            return {"message": f"Suck It And See song id {suckitandsee_id} already exists."}, 400
        data_post = SuckItAndSeeId.args.parse_args()
        new_song = SuckItAndSeeModel(suckitandsee_id, **data_post)
        try:
            new_song.save_song()
        except:
            return {'message': 'An internal error ocurred trying to save Suck It And See song.'}, 500
        return new_song.json(), 201  # Created

    @jwt_required()
    def put(self, suckitandsee_id):
        data_put = SuckItAndSeeId.args.parse_args()
        search_song = SuckItAndSeeModel.find_song(suckitandsee_id)
        if search_song:
            search_song.update_song(**data_put)
            search_song.save_song()
            return search_song.json(), 200

        new_song = SuckItAndSeeModel(suckitandsee_id, **data_put)
        try:
            new_song.save_song()
        except:
            return {'message': 'An internal error ocurred trying to save Suck It And See song.'}, 500
        return new_song.json(), 201  # Created

    @jwt_required()
    def delete(self, suckitandsee_id):
        song = SuckItAndSeeModel.find_song(suckitandsee_id)
        if song:
            try:
                song.delete_song()
            except:
                return {'message': 'An internal error ocurred trying to delete Suck It And See song.'}, 500
            return {'message': 'Suck It And See song deleted.'}, 404

