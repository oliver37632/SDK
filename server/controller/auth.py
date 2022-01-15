from server.model import session_scope
from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from server.model.user import User


def signup(id, name, password, school):
    with session_scope() as session:
        user = session.query(User).filter(User.id == id).first()
        if not user:
            new_sigup = User(
                id=id,
                name=name,
                password=generate_password_hash(password),
                school=school
            )
            session.add(new_sigup)
            session.commit()

            return {
                       "message": "success"
                   }, 201
        return {
            "message": "overlap"
        }, 403



def login(id, password):
    with session_scope() as session:
        user = session.query(User).filter(User.id == id)

        if not user.scalar():
            abort(409, 'user id code does not match')

        user = user.first()
        check_user_pw = check_password_hash(user.password, password)

        access_expires_delta = timedelta(minutes=60)
        refresh_expires_delta = timedelta(weeks=1)

        access_token = create_access_token(expires_delta=access_expires_delta,
                                           identity=id
                                           )
        refresh_token = create_refresh_token(expires_delta=refresh_expires_delta,
                                             identity=id
                                             )
        return {
                   'access_token': access_token,
                   'refresh_token': refresh_token
               }, 201

