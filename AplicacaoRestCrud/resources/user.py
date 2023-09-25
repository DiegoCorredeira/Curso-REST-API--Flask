from flask import json
from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):
    # refere-se /user/<int:user_id>
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'User not found': None}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': ''}, 500
            return {'message': 'User has deleted.'}, 404


class UserRegister(Resource):
    def post(self):
        # refere-se /user/register
        args = reqparse.RequestParser()
        args.add_argument('login', type=str, required=True,
                          help="The field 'login' cannot be left blank.")
        args.add_argument('password', type=str, required=True,
                          help="The field 'password' cannot be left blank.")
        data = args.parse_args()

        if UserModel.find_by_login(data['login']):
            return {"message": f"User {data['login']} already exists."}, 400

        user = UserModel(**data)
        user.save_user()

        return {"message": "User created successfully!"}, 201  # Created
