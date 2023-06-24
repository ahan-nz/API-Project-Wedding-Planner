from init import db, ma

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    postcode = db.Column(db.Integer, nullable=False)