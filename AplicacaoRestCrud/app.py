from flask import Flask, jsonify
from blacklist import BLACKLIST
from flask_restful import Api
from resources.WPSIATWIN import WPSAMTWINSongs, WPSAMTWINId
from resources.FWN import FWNSongs, FWNId
from resources.humbug import HumbugSongs, HumbugId
from resources.suckitandsee import SuckItAndSeeSongs, SuckItAndSeeId
from resources.user import User, UserLogin, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '6Zp#K9R$@W7y5mQ2X8L'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

@app.before_request
def create_db():
    db.create_all()

@jwt.token_in_blocklist_loader
def check_blacklist(self,token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def access_token_invalid():
    return jsonify({'message': 'You have been logged out.'}), 401 # Unauthorized

resources = [
    (HumbugSongs, '/humbug'),
    (HumbugId, '/humbug/<int:humbug_id>'),
    (WPSAMTWINSongs, '/WPSIATWIN'),
    (WPSAMTWINId, '/WPSIATWIN/<int:WPSIATWIN_id>'),
    (FWNSongs, '/FWN'),
    (FWNId, '/FWN/<int:FWN_id>'),
    (SuckItAndSeeSongs, '/suckitandsee'),
    (SuckItAndSeeId, '/suckitandsee/<int:suckitandsee_id>'),
    (User, '/user/<int:user_id>'),
    (UserRegister, '/register'), 
    (UserLogin, '/login'),
    (UserLogout, '/logout'), 
]
for resource, *routes in resources:
    api.add_resource(resource, *routes)

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
