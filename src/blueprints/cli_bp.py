from init import db, bcrypt
from models.user import User
from models.city import City
from models.state import State
from models.guest import Guest
from models.venue import Venue
from models.wedding import Wedding
from flask import Blueprint

cli_bp = Blueprint('db', __name__)

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
            is_admin=False
        ),
        User(
            f_name='Chris',
            l_name='Lee',
            email='chris@mymail.com',
            password=bcrypt.generate_password_hash('thisischris').decode('utf-8'),
            is_admin=False
        )
    ]

    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    states = [
        State(
            name='Victoria'
        ),
        State(
            name='Queensland'
        ),
        State(
            name='Tasmania'
        ),
        State(
            name='South Australia'
        ),
        State(
            name='New South Wales'
        ),
        State(
            name='Western Australia'
        )
    ]

    db.session.query(State).delete()
    db.session.add_all(states)
    db.session.commit()

    cities = [
        City(
            name='Mornington',
            postcode='3931',
            state_id=states[0].id
        ),
        City(
            name='Brookfield',
            postcode='4069',
            state_id=states[1].id
        ),
        City(
            name='Kingsford',
            postcode='5118',
            state_id=states[3].id
        ),
        City(
            name='Brookfield',
            postcode='4069',
            state_id=states[4].id
        ),
        City(
            name='Hagley',
            postcode='7292',
            state_id=states[2].id
        )
    ]

    db.session.query(City).delete()
    db.session.add_all(cities)
    db.session.commit()


    guests = [
        Guest(
            f_name='John',
            l_name='Smith',
            phone = '0400100200',
            email='john@johnsmith.com',
            is_rsvp=True,
            user_id=users[0].id
        ),
        Guest(
            f_name='Margaret',
            l_name='Connolly',
            phone = '0400100100',
            email='margaret@hello.com',
            user_id=users[1].id
        ),
        Guest(
            f_name='Richard',
            l_name='Han',
            phone = '0400100201',
            email='richardhan@sample.com',
            user_id=users[1].id
        ),
        Guest(
            f_name='Eddy',
            l_name='Chan',
            phone = '0434387110',
            email='beans@shibainu.com',
            is_rsvp=True,
            user_id=users[2].id
        ),
        Guest(
            f_name='Mary',
            l_name='Lamb',
            phone = '0400123456',
            email='marylamb@mail.com',
            user_id=users[2].id
        )
    ]

    db.session.query(Guest).delete()
    db.session.add_all(guests)
    db.session.commit()

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

    db.session.query(Venue).delete()
    db.session.add_all(venues)
    db.session.commit()

    weddings = [
        Wedding(
            date_of_wedding='2023-11-30',
            user_id=users[0].id
        ),
        Wedding(
            date_of_wedding='2024-05-12',
            user_id=users[1].id
        ),
        Wedding(
            date_of_wedding='2025-01-02',
            user_id=users[2].id
        )
    ]

    db.session.query(Wedding).delete()
    db.session.add_all(weddings)
    db.session.commit()

    print("Models seeded")