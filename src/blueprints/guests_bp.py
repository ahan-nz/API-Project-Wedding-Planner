from flask import Blueprint, request
from init import db
from models.guest import Guest, GuestSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required, admin_or_owner_required

# To add blueprint for guests and define the prefix for all URLs in this blueprint
guests_bp = Blueprint('guests', __name__, url_prefix='/guests')

# The following are CRUD routes for guests

# READ: Route for getting a list of all guests and their associated users, this is admin access only.
@guests_bp.route('/') # No method defined as GET is default
@jwt_required()
def all_guests():
    admin_required()
    stmt = db.select(Guest)
    guests = db.session.scalars(stmt).all()
    return GuestSchema(many=True).dump(guests)


# READ: Route for getting the information of a single guest, matched by the guest id in the URL in integer form, accessible by the admin and the user who 'owns', or created, the guest
@guests_bp.route('/<int:guest_id>')
@jwt_required()
def one_guest(guest_id):
    stmt = db.select(Guest).filter_by(id=guest_id)
    guest = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    if guest:
        admin_or_owner_required(guest.user.id)
        return GuestSchema().dump(guest)
    else:
        return {'error': 'Guest not found'}, 404 # Handles error of invalid guest id with a clear error message
    

# CREATE: Route for creating a new guest, with login required
@guests_bp.route('/', methods=['POST'])
@jwt_required()
def create_guest():
    # Parse, sanitize and validate the incoming JSON data via the schema
    guest_info = GuestSchema().load(request.json)

    # Create a new Guest model instance with the schema data
    guest = Guest(
        f_name = guest_info['f_name'],
        l_name = guest_info['l_name'],
        email = guest_info.get('email'), # Email is optional
        phone = guest_info.get('phone'), # Phone is optional, e.g. if guest is a child who doesn't have their own number
        is_rsvp = guest_info.get('is_rsvp'), # RSVP is false by default, hence entering it here is optional
        user_id = get_jwt_identity() # Automatically generated based on the token
    )

    db.session.add(guest)
    db.session.commit() # Adding the new guest to the database

    return GuestSchema().dump(guest), 201


# UPDATE: Modifying a guest's information, with the id in the URL, except for who the 'owner', or user_id, is.
@guests_bp.route('/<int:guest_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_guest(guest_id):
    stmt = db.select(Guest).filter_by(id=guest_id)
    guest = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    guest_info = GuestSchema().load(request.json) # Applies validation rules in schema
    if guest:
        admin_or_owner_required(guest.user.id) # Modification only accessible by admin and/or the user who 'owns', or created, the guest.
        guest.f_name = guest_info.get('f_name', guest.f_name) # This, and the following rows, are all optional. If not entered, then the original value will be kept.
        guest.l_name = guest_info.get('l_name', guest.l_name)
        guest.email = guest_info.get('email', guest.email)
        guest.phone = guest_info.get('phone', guest.phone)
        guest.is_rsvp = guest_info.get('is_rsvp', guest.is_rsvp)
        db.session.commit() # Finalizing the change in the database, don't need to add session as nothing new was created
        return GuestSchema().dump(guest)
    else:
       return {'error': 'Guest not found'}, 404 # Handles error of invalid guest id with a clear error message


# DELETE: This route allows the removal of a guest by the admin or the 'owner' of the guest
@guests_bp.route('/<int:guest_id>', methods=['DELETE'])
@jwt_required()
def delete_guest(guest_id):
    stmt = db.select(Guest).filter_by(id=guest_id)
    guest = db.session.scalar(stmt)
    if guest:
       admin_or_owner_required(guest.user.id)
       db.session.delete(guest)
       db.session.commit() # Finalising the deletion in the database
       return{}, 200 # Nothing returned as the guest was removed, with a 200 success response
    else:
       return {'error': 'Guest not found'}, 404 # Handles error of invalid guest id with a clear error message
