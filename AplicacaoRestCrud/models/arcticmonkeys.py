class HumbugModel:
    def __init__(self, id, title, artist, album, release_date, time):
        self.id = id
        self.title = title
        self.artist = artist
        self.album = album
        self.release_date = release_date
        self.time = time

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'release_date': self.release_date,
            'time': self.time
        }
