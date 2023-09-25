from flask import Flask
from flask_restful import Api
from resources.arcticmonkeys import HumbugSongs, HumbugId
from resources.user import User, UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_request
def create_db():
    db.create_all()


api.add_resource(HumbugSongs, '/humbug')
api.add_resource(HumbugId, '/humbug/<int:humbug_id>')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
