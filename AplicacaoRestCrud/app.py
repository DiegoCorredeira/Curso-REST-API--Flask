from flask import Flask
from flask_restful import  Api
from resources.arcticmonkeys import Humbug

app = Flask(__name__)
api = Api(app)



api.add_resource(Humbug, '/humbug')


if __name__ == '__main__':
    app.run(debug=True)
    