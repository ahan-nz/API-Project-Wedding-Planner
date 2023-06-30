from init import db, ma

# States entity added as this web app will only be applicable to Australian addresses for now

# SQLAlchemy creates table structure with columns and data types
class State(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    cities = db.relationship('City', back_populates='state', cascade='all, delete') # When a state is deleted, all cities in the state will be deleted


# JSON (de)serialization with Marshmallow
class StateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')