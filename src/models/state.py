from init import db, ma

class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    cities = db.relationship('City', back_populates='state', cascade='all, delete')


class StateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')