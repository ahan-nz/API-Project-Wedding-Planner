from flask import Flask
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp

def setup():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)

    return app