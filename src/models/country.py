from init import db, ma

class Country(db.Model):
    __tablename__ = 'coountries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))