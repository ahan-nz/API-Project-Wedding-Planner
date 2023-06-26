from init import db, ma
# from marshmallow import fields

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer)
    email = db.Column(db.String)
    is_rsvp = db.Column(db.Boolean, default=False)

class CitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'phone', 'email', 'is_rsvp')