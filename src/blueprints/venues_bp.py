from flask import Blueprint, request
from init import db
from models.venue import Venue, VenueSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

# To add blueprint for venues and define the prefix for all URLs in this blueprint
venues_bp = Blueprint('venues', __name__, url_prefix='/venues')

# The following are CRUD routes for venues

# READ: Route for getting a list of all venues
@venues_bp.route('/') # No method defined as GET is default
def all_venues():
    stmt = db.select(Venue)
    venues = db.session.scalars(stmt).all()
    return VenueSchema(many=True, exclude=['city_id']).dump(venues) # City id is excluded as city name will be returned anyway


# READ: Route for getting the information of one venue, specified by the venue id in the URL in integer form
@venues_bp.route('/<int:venue_id>')
def one_venue(venue_id):
    stmt = db.select(Venue).filter_by(id=venue_id)
    venue = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    if venue:
        return VenueSchema(exclude=['id', 'city_id']).dump(venue) # Venue id is already in the URL, and city id is excluded as city name will be returned
    else:
        return {'error': 'Venue not found'}, 404 # Handles error of invalid venue id with a clear error message
    

# CREATE: Route for creating a new venue, with login required
@venues_bp.route('/', methods=['POST'])
@jwt_required() # Only existing users can create new venues
def create_venue():
    try:
        # Parse, sanitize and validate the incoming JSON data via the schema
        venue_info = VenueSchema().load(request.json)

        # Create a new Venue model instance with the schema data
        venue = Venue(
            name = venue_info['name'],
            street_number = venue_info['street_number'],
            street_name = venue_info['street_name'],
            phone = venue_info['phone'],
            email = venue_info['email'],
            description = venue_info.get('description'), # This is optional. If not entered, will be null.
            cost_per_head = venue_info.get('cost_per_head'), # This is optional. If not entered, will be null.
            min_guests = venue_info.get('min_guests'), # This is optional. If not entered, will be null.
            max_guests = venue_info.get('max_guests'), # This is optional. If not entered, will be null.
            city_id = venue_info['city_id']
        )

        db.session.add(venue)
        db.session.commit() # Finalising the addition of the new venue to the database

        return VenueSchema(exclude=['city_id']).dump(venue), 201 # City id is excluded as city name will be returned anyway
    except IntegrityError: # Integrity error in a try except block, handles invalid city id with a clear error message.
        return {'error': 'City ID does not exist.'}, 400


# UPDATE: Modifying a venue's information, with the id in the URL, login required.
@venues_bp.route('/<int:venue_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Only existing users can modify venue information
def update_venue(venue_id):
    try:
        stmt = db.select(Venue).filter_by(id=venue_id)
        venue = db.session.scalar(stmt)
        venue_info = VenueSchema().load(request.json) # Applies validation rules in schema
        if venue:
            venue.name = venue_info.get('name', venue.name) # This, and the following rows, are all optional. If not entered, then the original value will be kept.
            venue.street_number = venue_info.get('street_number', venue.street_number)
            venue.street_name = venue_info.get('street_name', venue.street_name)
            venue.phone = venue_info.get('phone', venue.phone)
            venue.email = venue_info.get('email', venue.email)
            venue.description = venue_info.get('description', venue.description)
            venue.cost_per_head = venue_info.get('cost_per_head', venue.cost_per_head)
            venue.min_guests = venue_info.get('min_guests', venue.min_guests)
            venue.max_guests = venue_info.get('max_guests', venue.max_guests)
            venue.city_id = venue_info.get('city_id', venue.city_id)
            db.session.commit() # Finalizing the change in the database, don't need to add session as nothing new was created
            return VenueSchema(exclude=['city_id']).dump(venue) # City id is excluded as city name will be returned anyway
        else:
            return {'error': 'Venue not found'}, 404 # Handles error of invalid venue id with a clear error message
    except IntegrityError: # Integrity error in a try except block, handles invalid city id with a clear error message.
        return {'error': 'City ID does not exist.'}, 400


# DELETE: Removing a venue, with the id in the URL, login required.
@venues_bp.route('/<int:venue_id>', methods=['DELETE'])
@jwt_required() # Only existing users can delete venues
def delete_venue(venue_id):
    stmt = db.select(Venue).filter_by(id=venue_id)
    venue = db.session.scalar(stmt)
    if venue:
       db.session.delete(venue)
       db.session.commit() # Finalising the deletion in the database
       return{}, 200 # Nothing returned as the venue was removed, with a 200 success response
    else:
       return {'error': 'Venue not found'}, 404 # Handles error of invalid venue id with a clear error message