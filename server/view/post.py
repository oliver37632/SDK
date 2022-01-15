from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.controller.post import post, get, allget, SearchCategory

from datetime import datetime


class Post(Resource):
    @jwt_required()
    def post(self):
        title = request.form["title"]
        content = request.form["content"]
        category = request.form["category"]
        file = request.files["image"]
        file.save("./temp")
        id = get_jwt_identity()

        return post(
            title=title,
            content=content,
            category=category,
            id=id
        )


    def get(self):
        return allget()


class GetPost(Resource):
    @jwt_required()
    def get(self, id):
        return get(
            id=id
        )


class Category(Resource):
    def post(self):
        category = request.json["category"]

        return SearchCategory(
            category=category
        )

