from init import db, bcrypt
from models.user import User
from models.city import City
from models.state import State
from models.guest import Guest
from models.venue import Venue
from models.wedding import Wedding

@cli_bp.cli.command("create")
def create_db():
    db.drop_all()
    db.create_all()
    print("Tables created successfully")

@cli_bp.cli.command("seed")
def seed_db():
    users = [
        User(
            f_name='admin',
            l_name='admin',
            email='admin@weddings.com',
            password=bcrypt.generate_password_hash('adminplanner').decode('utf-8'),
            is_admin=True
        ),
        User(
            f_name='Sally',
            l_name='Smith',
            email='hello@sallysmith.com',
            password=bcrypt.generate_password_hash('weddingcake').decode('utf-8'),
            is_admin=True
        )
    ]

    cities = [
        City(
            name='Mornington',
            postcode='3931'
        ),
        City(
            name='Brookfield',
            postcode='4069'
        )
    ]

    states = [
        State(
            name='Victoria',
        ),
        State(
            name='Queensland',
        ),
        State(
            name='Tasmania'
        )
    ]

    db.session.add_all()
    db.session.commit()

    print("Models seeded")