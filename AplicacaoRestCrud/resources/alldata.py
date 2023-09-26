from flask_restful import Resource
from resources.humbug import HumbugSongs
from resources.WPSIATWIN import WPSAMTWINSongs
from resources.FWN import FWNSongs
from resources.suckitandsee import SuckItAndSeeSongs


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
