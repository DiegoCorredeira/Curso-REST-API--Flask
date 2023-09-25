from requests import delete
from sql_alchemy import db


class FWNModel(db.Model):
    __tablename__ = 'FWNSongs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    artist = db.Column(db.String(80))
    album = db.Column(db.String(80))
    release_date = db.Column(db.String(30))
    time = db.Column(db.String(80))
    

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
    
    @classmethod
    def find_song(cls, song_id):
        song = cls.query.filter_by(id=song_id).first() # Select * from songs where id = $id 
        if song:
            return song
        return None
    
    def save_song(self):
        db.session.add(self)
        db.session.commit()
        
    def update_song(self, title, artist, album, release_date, time):
        self.title = title
        self.artist = artist
        self.album = album
        self.release_date = release_date
        self.time = time
    
    def delete_song(self):
        db.session.delete(self)
        db.session.commit()