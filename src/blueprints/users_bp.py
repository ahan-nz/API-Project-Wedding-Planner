from flask import Blueprint, request
from models.user import User, UserSchema
from init import db, bcrypt
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required, admin_or_owner_required

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Get all users
@users_bp.route('/')
@jwt_required()
def all_users():
    admin_required()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)
    

# Update user account
@users_bp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    user_info = UserSchema().load(request.json)
    if user:
        admin_or_owner_required(user.id)
        user.f_name = user_info.get('f_name', user.f_name)
        user.l_name = user_info.get('l_name', user.l_name)
        user.email = user_info.get('email', user.email)
        user.password = bcrypt.generate_password_hash(user_info.get('password', user.password)).decode('utf-8')
        user.is_admin = user_info.get('is_admin', user.is_admin)
        db.session.commit()
        return UserSchema(exclude=['password', 'id']).dump(user)
    else:
       return {'error': 'User not found'}, 404
    

# Delete a user
@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
       admin_or_owner_required(user.id)
       db.session.delete(user)
       db.session.commit()
       return{}, 200
    else:
       return {'error': 'User not found'}, 404