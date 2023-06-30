from init import db, ma
from marshmallow import fields

# SQLAlchemy creates table structure with columns and data types
class City(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    postcode = db.Column(db.Integer, nullable=False)

    state_id = db.Column(db.Integer, db.ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
    state = db.relationship('State', back_populates='cities') # No cascade delete as the state shouldn't be deleted when a city is deleted
    venues = db.relationship('Venue', back_populates='city', cascade='all, delete') # When a city is deleted, all venues in the city will also be deleted

# JSON (de)serialization with Marshmallow
class CitySchema(ma.Schema):
    state = fields.Nested('StateSchema', exclude=['id'])

    class Meta:
        fields = ('id', 'name', 'postcode', 'state')
