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
            name='Victoria'
        ),
        State(
            name='Queensland'
        ),
        State(
            name='Tasmania'
        )
    ]

    guests = [
        Guest(
            f_name='John',
            l_name='Smith',
            phone = '0400100200',
            email='john@johnsmith.com',
            is_rsvp=True
        ),
        Guest(
            f_name='Margaret',
            l_name='Connolly',
            phone = '0400100100',
            email='margaret@hello.com'
        ),
        Guest(
            f_name='Richard',
            l_name='Han',
            phone = '0400100201',
            email='richardhan@sample.com'
        ),
        Guest(
            f_name='Eddy',
            l_name='Chan',
            phone = '0434387110',
            email='beans@shibainu.com',
            is_rsvp=True
        )
    ]

    venues = [
        Venue(
            name='Bundaleer Rainforest Gardens',
            street_number='59',
            street_name='Bundaleer St',
            phone='0733741360',
            email='hello@bundaleer.com',
            cost_per_head='190',
            min_guests='80',
            max_guests='200'
        ),
        Venue(
            name='Dalywaters Roses Garden and Chapel',
            street_number='240',
            street_name='Bungower Rd',
            phone='0425608264',
            email='hello@dalywaters.com',
            cost_per_head='220',
            min_guests='50',
            max_guests='150'
        )
    ]

    weddings = [
        Wedding(
            date='2023-11-30'
        ),
        Wedding(
            date='2024-05-12'
        )
    ]

    db.session.add_all()
    db.session.commit()

    print("Models seeded")