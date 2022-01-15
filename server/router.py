from flask import Blueprint
from flask_restful import Api

bp = Blueprint("among", __name__, url_prefix="")
api_basic = Api(bp)

from server.view.post import Post
api_basic.add_resource(Post, "/post")

from server.view.post import GetPost
api_basic.add_resource(GetPost, "/post/<int:id>")

from server.view.auth import SignUp
api_basic.add_resource(SignUp, "/signup")

from server.view.auth import Login
api_basic.add_resource(Login, "/login")

from server.view.post import Category
api_basic.add_resource(Category, "/post/category")