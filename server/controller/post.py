from server.model import session_scope
from server.model.post import Post
from server.model.user import User

from flask import abort, request

from server.model.S3 import s3_put_object, s3_connection
from server.config import AWS_S3_BUCKET_NAME

from datetime import datetime

s3 = s3_connection()


def post(title, content, category, id):
    with session_scope() as session:
        name = title
        s3_put_object(s3, AWS_S3_BUCKET_NAME, "./temp", name)
        location = s3.get_bucket_location(Bucket=AWS_S3_BUCKET_NAME)['LocationConstraint']
        image_url = f'https://{AWS_S3_BUCKET_NAME}.s3.{location}.amazonaws.com/{name}'
        count = User.count+1
        new_post = Post(
            title=title,
            content=content,
            category=category,
            image=image_url,
            id=id,
            create_at=datetime.now(),
            userId=id
        )

        session.add(new_post)
        session.commit()

        return{
            "message": "success"
        }, 201


def allget():
    with session_scope() as session:
        posts = session.query(
            Post.id,
            Post.title,
            Post.content,
            Post.category,
            Post.image,
            User.id
        ).join(User, User.id == Post.userId)

        if posts:
            return {
                       "posts": [{
                           "id": id,
                           "title": title,
                           "content": content,
                           "category": category,
                           "image": image,
                           "user": user
                       } for id, title, content, category, image, user in posts]
                   }, 200

        return abort(404, "Not Found")


def get(id):
    with session_scope() as session:
        posts = session.query(
            Post.title,
            Post.content,
            Post.category,
            Post.image,
            User.id
        ).join(User, User.id == Post.userId).filter(Post.id == id)

        if posts:
            return {
                       "posts": [{
                           "title": title,
                           "content": content,
                           "category": category,
                           "image": image,
                           "user": user
                       } for title, content, category, image, user in posts]
                   }, 200

        return abort(404, "Not Found")


def SearchCategory(category):
    with session_scope() as session:
        posts = session.query(
            Post.id,
            Post.title,
            Post.content,
            Post.image,
            User.id
        ).join(User, User.id == Post.userId).filter(Post.category == category)

        if posts:
            return {   "category": category,
                       "posts": [{
                           "id": id,
                           "title": title,
                           "content": content,
                           "image": image,
                           "user": user
                       } for id, title, content, image, user in posts]
                   }, 200

        return abort(404, "Not Found")
