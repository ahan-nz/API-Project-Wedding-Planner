from flask import Blueprint
from models.user import User, UserSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/users')
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)