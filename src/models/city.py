from init import db, ma
from marshmallow import fields

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    postcode = db.Column(db.Integer, nullable=False)

    state_id = db.Column(db.Integer, db.ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
    state = db.relationship('State', back_populates='cities')
    venues = db.relationship('Venue', back_populates='city', cascade='all, delete')

class CitySchema(ma.Schema):
    state = fields.Nested('StateSchema', exclude=['id'])

    class Meta:
        fields = ('id', 'name', 'postcode', 'state')
