from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    wedding = db.relationship('Wedding', back_populates='user', cascade='all, delete')


class UserSchema(ma.Schema):
    wedding = fields.Nested('WeddingSchema', exclude=['user', 'id'])

    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email', 'password', 'is_admin', 'wedding')