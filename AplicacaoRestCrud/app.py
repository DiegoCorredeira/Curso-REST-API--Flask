from flask import Flask
from flask_restful import Api
from resources.FWN import FWNSongs, FWNId
from resources.WPSIATWIN import WPSAMTWINSongs, WPSAMTWINId
from resources.humbug import HumbugSongs, HumbugId
from resources.user import User, UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_request
def create_db():
    db.create_all()


resources = [
    (HumbugSongs, '/humbug'),
    (HumbugId, '/humbug/<int:humbug_id>'),
    (WPSAMTWINSongs, '/WPSIATWIN'),
    (WPSAMTWINId, '/WPSIATWIN/<int:WPSIATWIN_id>'),
    (FWNSongs, '/FWN'),
    (FWNId, '/FWN/<int:FWN_id>'),
    (User, '/user/<int:user_id>'),
    (UserRegister, '/register')
]
for resource, *routes in resources:
    api.add_resource(resource, *routes)

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
