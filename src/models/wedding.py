from init import db, ma

class Wedding(db.Model):
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())