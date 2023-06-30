from flask import Blueprint, request, abort
from models.user import User, UserSchema
from init import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import timedelta

# This blueprint utilizes the User model and schema to allow user registration and logins
auth_bp = Blueprint('auth', __name__)

# This is the route for creating a new user in the database
@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        # Parse, sanitize and validate the incoming JSON data via the schema
        user_info = UserSchema().load(request.json)
        # Create a new user instance from the user information
        user = User(
            email=user_info['email'],
            password=bcrypt.generate_password_hash(user_info['password']).decode('utf-8'),
            f_name=user_info['f_name'],
            l_name=user_info['l_name']
        )

        # Adding and committing the new user to the database
        db.session.add(user)
        db.session.commit()

        return UserSchema(exclude=['password']).dump(user), 201 # Send new user back to client, keeping the password hidden for better security
    except IntegrityError: # This error avoids duplicate accounts with the same email, handled with a clear error message
        return {'error': 'Email address already in use'}, 409
    

# This is the route for letting users login with their email and password
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email']) # Select user with a matching email address as the request
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            token = create_access_token(identity=user.id, expires_delta=timedelta(hours=12)) # This token will expire after 12 hours, after which a user must login in again to generate a new token
            return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
        else:
            return {'error': 'Invalid email address or password'}, 401 # Not specifying which was incorrect for better security
    except KeyError: # This error is to ensure both email and password are entered, handled with a clear error message
        return {'error': 'Email and password are required'}, 400


# This function to check if users are an admin before being authorized to access certain endpoints
def admin_required():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401, description="You must be an admin") # This will terminate the request response cycle and send a clear error message to the user


# This function is to check if a user either created/owns the data being queried before being allowed access, or has admin rights.
def admin_or_owner_required(owner_id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and (user.is_admin or user_id == owner_id)):
        abort(401, description="You must be an admin or user") # This will terminate the request response cycle and send a clear error message to the user