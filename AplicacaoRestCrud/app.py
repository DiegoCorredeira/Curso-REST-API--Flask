from flask import Flask
from flask_restful import Api
from resources.arcticmonkeys import HumbugSongs, HumbugId

app = Flask(__name__)
api = Api(app)

api.add_resource(HumbugSongs, '/humbug')
api.add_resource(HumbugId, '/humbug/<int:humbug_id>')

if __name__ == '__main__':
    app.run(debug=True)
