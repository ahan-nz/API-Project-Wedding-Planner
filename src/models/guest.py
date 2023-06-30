from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer)
    email = db.Column(db.String)
    is_rsvp = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='guests')


class GuestSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])
    f_name = fields.String(required=True, validate=And(Length(min=1, error='First name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    l_name = fields.String(required=True, validate=And(Length(min=1, error='Last name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    phone= fields.String(required = True, validate= Regexp('^[0-9 ()+]+$', error="Please provide a valid phone number"))
    email = fields.String(required = True, validate= Regexp('^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', error="Please provide a valid email address"))
    is_rsvp = fields.Boolean(load_default=False)

    class Meta:
        fields = ('id', 'f_name', 'l_name', 'phone', 'email', 'is_rsvp', 'user')