from init import db, ma
# from marshmallow import fields

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    postcode = db.Column(db.Integer, nullable=False)

class CitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'postcode')