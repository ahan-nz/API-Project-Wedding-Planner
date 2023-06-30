from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    wedding = db.relationship('Wedding', back_populates='user', cascade='all, delete')
    guests = db.relationship('Guest', back_populates='user', cascade='all, delete')


class UserSchema(ma.Schema):
    f_name = fields.String(required=True, validate=And(Length(min=1, error='First name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    l_name = fields.String(required=True, validate=And(Length(min=1, error='Last name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    password = fields.String(load_only=True, validate= Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[#+-=@$!%*?&])[A-Za-z\d@$#$^()!%*?&]{8,}$', error='Password must contain a minimum of eight characters, at least one uppercase letter, one lowercase letter, one number and one special character.'))
    email = fields.String(required = True, validate= Regexp('^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', error="Please provide a valid email address"))
    is_admin = fields.Boolean(load_default=False)
    
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email', 'password', 'is_admin')