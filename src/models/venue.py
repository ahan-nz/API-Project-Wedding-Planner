from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text())
    cost_per_head = db.Column(db.Integer)
    min_guests = db.Column(db.Integer)
    max_guests = db.Column(db.Integer)

    city_id = db.Column(db.Integer, db.ForeignKey('cities.id', ondelete='CASCADE'), nullable=False)
    city = db.relationship('City', back_populates='venues')
    weddings = db.relationship('Wedding', back_populates='venue')


class VenueSchema(ma.Schema):
    city = fields.Nested('CitySchema', exclude=['id'])
    name = fields.String(validate=Length(min=1, error='Name of venue needs at least one character.'))
    street_number = fields.Integer()
    street_name = fields.String(validate=Length(min=2, error='Street name needs at least two characters.'))
    phone= fields.String(validate= Regexp('^[0-9 ()+]+$', error="Please provide a valid phone number"))
    email = fields.String(validate= Regexp('^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', error="Please provide a valid email address"))
    cost_per_head = fields.Integer()
    min_guests = fields.Integer()
    max_guests = fields.Integer()
    city_id = fields.Integer()

    class Meta:
        fields = ('id', 'name', 'street_number', 'street_name', 'phone', 'email', 'description', 'cost_per_head', 'min_guests', 'max_guests', 'city_id', 'city')
        ordered = True