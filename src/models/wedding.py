from init import db, ma
from marshmallow import fields

class Wedding(db.Model):
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    date_of_wedding = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    user = db.relationship('User', back_populates='wedding')
    venue = db.relationship('Venue', back_populates='weddings')


class WeddingSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])
    venue = fields.Nested('VenueSchema', only=['name', 'city'])
    date_of_wedding = fields.Date(load_default=None)
    venue_id = fields.Integer(load_default=None)

    class Meta:
        fields = ('id', 'date_of_wedding', 'user', 'venue_id', 'venue')
