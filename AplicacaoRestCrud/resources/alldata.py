from os import path
from flask_restful import Resource, reqparse
from pkg_resources import RequirementParseError
from resources.humbug import HumbugSongs
from resources.WPSIATWIN import WPSAMTWINSongs
from resources.FWN import FWNSongs
from resources.suckitandsee import SuckItAndSeeSongs
import sqlite3

path_params = reqparse.RequestParser()
path_params.add_argument('title', type=str, )
path_params.add_argument('artist', type=str)
path_params.add_argument('album', type=str)
path_params.add_argument('shortest_song', type=str)
path_params.add_argument('longest_song', type=str)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)


def normalize_path_params(title=None, artist=None, album=None, shortest_song=None, longest_song=None, limit=15, offset=0, **dados):
    if title:
        return {
            'artist': artist,
            'album': album,
            'shortest_song': shortest_song,
            'longest_song': longest_song,
            'limit': limit,
            'offset': offset
        }
    return {
        'title': None,
        'artist': None,
        'album': None,
        'shortest_song': None,
        'longest_song': None,
        'limit': limit,
        'offset': offset
    }
    


class AllData(Resource):
    def get(self):
    
        humbug_songs_resource = HumbugSongs()
        wpsiatwin_songs_resource = WPSAMTWINSongs()
        fwn_songs_resource = FWNSongs()
        suckitandsee_songs_resource = SuckItAndSeeSongs()

        humbug_songs = humbug_songs_resource.get()
        wpsiatwin_songs = wpsiatwin_songs_resource.get()
        fwn_songs = fwn_songs_resource.get()
        suckitandsee_songs = suckitandsee_songs_resource.get()

        all_data = {
            'humbug_songs': {'All Humbug Songs': humbug_songs},
            'wpsiatwin_songs': {'Whatever People Say I am, That\'s What I\'m Not Songs': wpsiatwin_songs},
            'fwn_songs': {'Favourite Worst Nightmare Songs': fwn_songs},
            'suckitandsee_songs': {'Suck It And See Songs': suckitandsee_songs},
        }

        return all_data
