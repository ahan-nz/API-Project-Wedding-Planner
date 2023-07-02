from flask import Blueprint, request
from init import db
from models.wedding import Wedding, WeddingSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required, admin_or_owner_required
from sqlalchemy.exc import IntegrityError

# To add blueprint for weddings and define the prefix for all URLs in this blueprint
weddings_bp = Blueprint('weddings', __name__, url_prefix='/weddings')

# The following are CRUD routes for weddings

# READ: Route for getting a list of all wedings, this is admin access only.
@weddings_bp.route('/')
@jwt_required()
def all_weddings():
    admin_required()
    stmt = db.select(Wedding)
    weddings = db.session.scalars(stmt).all()
    return WeddingSchema(many=True, exclude=['venue_id']).dump(weddings) # Venue id excluded as venue name will be returned anyway


# READ: Route for getting the information of a single wedding entry, matched by the id in the URL in integer form, accessible by the admin and the user who 'owns' the wedding entry
@weddings_bp.route('/<int:wedding_id>')
@jwt_required()
def one_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id)
    wedding = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    if wedding:
        admin_or_owner_required(wedding.user.id)
        return WeddingSchema(exclude=['id', 'venue_id']).dump(wedding) # Wedding id is in the URL, venue id excluded as venue name will be returned anyway
    else:
        return {'error': 'Wedding entry not found'}, 404 # Handles error of invalid wedding id with a clear error message
    

# CREATE: Route for creating a new wedding entry, with login required
@weddings_bp.route('/', methods=['POST'])
@jwt_required()
def create_wedding():
    try:
        # Parse, sanitize and validate the incoming JSON data via the schema
        wedding_info = WeddingSchema().load(request.json)

        # Create a new Wedding model instance with the schema data
        wedding = Wedding(
            date_of_wedding = wedding_info.get('date_of_wedding'), # Optional, will be null if left blank
            user_id = get_jwt_identity(), # Automatically generated based on the token
            venue_id = wedding_info.get('venue_id') # Optional, will be null if left blank
        )

        db.session.add(wedding)
        db.session.commit() # Finalising the addition of the new wedding entry into the database

        return WeddingSchema(exclude=['venue_id']).dump(wedding), 201 # Venue id excluded as venue name will be returned anyway
    except IntegrityError: # Integrity error in a try except block, handles invalid venue id with a clear error message.
        return {'error': 'Venue entered does not exist.'}, 400


# UPDATE: Modifying a wedding entry's information, with the id in the URL
@weddings_bp.route('/<int:wedding_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_wedding(wedding_id):
    try:
        stmt = db.select(Wedding).filter_by(id=wedding_id)
        wedding = db.session.scalar(stmt) # Singular scalar as only one instance is expected
        wedding_info = WeddingSchema().load(request.json) # Applies validation rules in schema
        if wedding:
            admin_or_owner_required(wedding.user.id) # Accessible by admin or the owner of the wedding entry only
            wedding.date_of_wedding = wedding_info.get('date_of_wedding', wedding.date_of_wedding) # Optional. If not entered, then the original value will be kept.
            wedding.venue_id = wedding_info.get('venue_id', wedding.venue_id) # Optional. If not entered, then the original value will be kept.
            db.session.commit() # Finalizing the change in the database, don't need to add session as nothing new was created
            return WeddingSchema(exclude=['venue_id']).dump(wedding) # Venue id excluded as venue name will be returned anyway
        else:
            return {'error': 'Wedding entry not found'}, 404 # Handles error of invalid wedding id with a clear error message
    except IntegrityError: # Integrity error in a try except block, handles invalid venue id with a clear error message.
        return {'error': 'Venue entered does not exist.'}, 400


# DELETE: This route allows the removal of a wedding entry by the admin or the 'owner'
@weddings_bp.route('/<int:wedding_id>', methods=['DELETE'])
@jwt_required()
def delete_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id)
    wedding = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    if wedding:
       admin_or_owner_required(wedding.user.id)
       db.session.delete(wedding) 
       db.session.commit() # Finalising the deletion in the database
       return{}, 200 # Nothing returned as the wedding entry was removed, with a 200 success response
    else:
       return {'error': 'Wedding entry not found'}, 404 # Handles error of invalid wedding id with a clear error message