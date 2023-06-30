from flask import Blueprint, request
from models.user import User, UserSchema
from init import db, bcrypt
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required, admin_or_owner_required

# To add blueprint for users and define the prefix for all URLs in this blueprint
users_bp = Blueprint('users', __name__, url_prefix='/users')

# The following are CRUD routes for users, except for creating a user, which is inside auth_bp under '/register'

# READ: Route for getting a list of all users, excluding the password for security, this is admin access only.
@users_bp.route('/')
@jwt_required()
def all_users():
    admin_required()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)
    

# UPDATE: Modifying a user's information, with the id in the URL, only accessible by admin or the user themselves.
@users_bp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    user_info = UserSchema().load(request.json) # Applies validation rules in schema
    if user:
        admin_or_owner_required(user.id)
        user.f_name = user_info.get('f_name', user.f_name) # This, and the following rows, are all optional. If not entered, then the original value will be kept.
        user.l_name = user_info.get('l_name', user.l_name)
        user.email = user_info.get('email', user.email)
        user.password = bcrypt.generate_password_hash(user_info.get('password', user.password)).decode('utf-8')
        user.is_admin = user_info.get('is_admin', user.is_admin)
        db.session.commit() # Finalizing the change in the database, don't need to add session as nothing new was created
        return UserSchema(exclude=['password', 'id']).dump(user) # Password is excluded for security reasons, and ID is already in the URL.
    else:
       return {'error': 'User not found'}, 404 # Handles error of invalid user id with a clear error message
    

# DELETE: This route allows the removal of a user by the admin or the user themselves
@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
       admin_or_owner_required(user.id)
       db.session.delete(user)
       db.session.commit() # Finalising the deletion in the database
       return{}, 200 # Nothing returned as the user was removed, with a 200 success response
    else:
       return {'error': 'User not found'}, 404 # Handles error of invalid user id with a clear error message