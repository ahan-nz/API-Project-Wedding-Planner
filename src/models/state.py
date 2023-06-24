from init import db, ma

class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))