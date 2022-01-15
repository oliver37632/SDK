from flask import request
from flask_restful import Resource
from server.controller.auth import signup, login


class SignUp(Resource):
    def post(self):
        id = request.json['id']
        name = request.json['name']
        password = request.json['password']
        school= request.json['school']

        return signup(
                id=id,
                name=name,
                password=password,
                school=school
        )


class Login(Resource):
    def post(self):
        id = request.json['id']
        password = request.json['password']

        return login(
            id=id,
            password=password
        )


