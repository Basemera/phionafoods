from flask_restful import Resource, reqparse
from flask import redirect, url_for, logging, jsonify
# from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
# from passlib.hash import pbkdf2_sha256 as sha256
from app.models import Users

class user_registration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        parser.add_argument('email', help='This field cannot be blank', required=True)
        parser.add_argument('password', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        user_name = data["username"].strip()
        email = data["email"].strip()
        password = data["password"].strip()

        if user_name == "" or email == "" or  password == "":
            return jsonify({"Error": "Fields have not been filled"}), 400
        else:
            t = tuple(user_name)
            if  t[0].isdigit():
                return jsonify({"error": "username cant be string"}), 400
            else:
                # password_candidste = Users.generate_hash(password)
                new_user = Users(user_name,password,email)

                # user_data = {"username": user_name.lower(), "email": email, "password": password_candidste}

                return new_user.check_user()