from flask import Flask 
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.weddings_bp import weddings_bp
from blueprints.guests_bp import guests_bp
from blueprints.venues_bp import venues_bp
from blueprints.users_bp import users_bp
from marshmallow.exceptions import ValidationError

def setup():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.json.sort_keys = False

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
    
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400
    
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.__dict__['messages']}, 400

    # Registering blueprints to run with "flask run"
    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(weddings_bp)
    app.register_blueprint(guests_bp)
    app.register_blueprint(venues_bp)
    app.register_blueprint(users_bp)

    return app