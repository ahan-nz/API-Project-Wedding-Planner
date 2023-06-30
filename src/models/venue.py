from init import db, ma
from marshmallow import fields

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
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

    class Meta:
        fields = ('id', 'name', 'street_number', 'street_name', 'phone', 'email', 'description', 'cost_per_head', 'min_guests', 'max_guests', 'city_id', 'city')
        # ordered = True