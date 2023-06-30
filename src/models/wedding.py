from init import db, ma
from marshmallow import fields

# SQLAlchemy creates table structure with columns and data types
class Wedding(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    date_of_wedding = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    user = db.relationship('User', back_populates='wedding') # No cascade delete as when a wedding entry is deleted, the user shouldn't be deleted.
    venue = db.relationship('Venue', back_populates='weddings') # No cascade delete as when a wedding entry is deleted, the venue shouldn't be deleted.


# JSON (de)serialization with Marshmallow
class WeddingSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])
    venue = fields.Nested('VenueSchema', only=['name', 'city'])
    date_of_wedding = fields.Date()
    venue_id = fields.Integer()

    class Meta:
        fields = ('id', 'date_of_wedding', 'user', 'venue_id', 'venue')
        ordered = True # Orders keys in the same order as above
