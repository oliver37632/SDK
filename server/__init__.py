from flask import Flask
from flask_jwt_extended import JWTManager

from server.router import bp
from server.config import secret, ACCESS_TIMEOUT, REFRESH_TIMEOUT

def create_app():
    _app = Flask(__name__)

    jwt = JWTManager(_app)

    _app.secret_key = secret
    _app.config['JWT_ACCESS_TOKEN_EXPIRES'] = ACCESS_TIMEOUT
    _app.config['JWT_REFRESH_TOKEN_EXPIRES'] = REFRESH_TIMEOUT
    _app.register_blueprint(bp)

    return _app
