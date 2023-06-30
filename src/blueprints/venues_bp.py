from flask import Blueprint, request
from init import db
from models.venue import Venue, VenueSchema
from flask_jwt_extended import jwt_required

venues_bp = Blueprint('venues', __name__, url_prefix='/venues')


# Get all venues
@venues_bp.route('/')
def all_venues():
    stmt = db.select(Venue)
    venues = db.session.scalars(stmt).all()
    return VenueSchema(many=True, exclude=['city_id']).dump(venues)


# Get one venue
@venues_bp.route('/<int:venue_id>')
def one_venue(venue_id):
    stmt = db.select(Venue).filter_by(id=venue_id)
    venue = db.session.scalar(stmt)
    if venue:
        return VenueSchema(exclude=['id', 'city_id']).dump(venue)
    else:
        return {'error': 'Venue not found'}, 404
    

# Create a new venue
@venues_bp.route('/', methods=['POST'])
@jwt_required()
def create_venue():
    venue_info = VenueSchema().load(request.json)

    venue = Venue(
        name = venue_info['name'],
        street_number = venue_info['street_number'],
        street_name = venue_info['street_name'],
        phone = venue_info['phone'],
        email = venue_info['email'],
        description = venue_info.get('description'),
        cost_per_head = venue_info.get('cost_per_head'),
        min_guests = venue_info.get('min_guests'),
        max_guests = venue_info.get('max_guests'),
        city_id = venue_info['city_id']
    )

    db.session.add(venue)
    db.session.commit()

    return VenueSchema(exclude=['city_id']).dump(venue), 201


# Update a venue
@venues_bp.route('/<int:venue_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_venue(venue_id):
    stmt = db.select(Venue).filter_by(id=venue_id)
    venue = db.session.scalar(stmt)
    venue_info = VenueSchema().load(request.json)
    if venue:
        venue.name = venue_info.get('name', venue.name)
        venue.street_number = venue_info.get('street_number', venue.street_number)
        venue.street_name = venue_info.get('street_name', venue.street_name)
        venue.phone = venue_info.get('phone', venue.phone)
        venue.email = venue_info.get('email', venue.email)
        venue.description = venue_info.get('description', venue.description)
        venue.cost_per_head = venue_info.get('cost_per_head', venue.cost_per_head)
        venue.min_guests = venue_info.get('min_guests', venue.min_guests)
        venue.max_guests = venue_info.get('max_guests', venue.max_guests)
        venue.city_id = venue_info.get('city_id', venue.city_id)
        db.session.commit()
        return VenueSchema(exclude=['city_id']).dump(venue)
    else:
       return {'error': 'Venue not found'}, 404


# Delete a venue
@venues_bp.route('/<int:venue_id>', methods=['DELETE'])
@jwt_required()
def delete_venue(venue_id):
    stmt = db.select(Venue).filter_by(id=venue_id)
    venue = db.session.scalar(stmt)
    if venue:
       db.session.delete(venue)
       db.session.commit()
       return{}, 200
    else:
       return {'error': 'Venue not found'}, 404