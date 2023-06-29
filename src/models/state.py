from init import db, ma
from marshmallow import fields

class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    cities = db.relationship('City', back_populates='state', cascade='all, delete')


class StateSchema(ma.Schema):
    cities = fields.List(fields.Nested('CitySchema', exclude=['id', 'state']))

    class Meta:
        fields = ('id', 'name', 'cities')