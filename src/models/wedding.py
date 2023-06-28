from init import db, ma
from marshmallow import fields

class Wedding(db.Model):
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    date_of_wedding = db.Column(db.Date())

class WeddingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_of_wedding')