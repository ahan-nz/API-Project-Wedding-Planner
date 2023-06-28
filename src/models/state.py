from init import db, ma
# from marshmallow import fields

class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class StateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')