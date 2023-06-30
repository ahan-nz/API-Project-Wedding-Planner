from flask import Blueprint, request
from init import db
from models.guest import Guest, GuestSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required, admin_or_owner_required

guests_bp = Blueprint('guests', __name__, url_prefix='/guests')


# Get all guests
@guests_bp.route('/')
@jwt_required()
def all_guests():
    admin_required()
    stmt = db.select(Guest)
    guests = db.session.scalars(stmt).all()
    return GuestSchema(many=True).dump(guests)


# Get one guest
@guests_bp.route('/<int:guest_id>')
@jwt_required()
def one_guest(guest_id):
    stmt = db.select(Guest).filter_by(id=guest_id)
    guest = db.session.scalar(stmt)
    if guest:
        admin_or_owner_required(guest.user.id)
        return GuestSchema().dump(guest)
    else:
        return {'error': 'Guest not found'}, 404
    

# Create a new guest
@guests_bp.route('/', methods=['POST'])
@jwt_required()
def create_guest():
    guest_info = GuestSchema().load(request.json)

    guest = Guest(
        f_name = guest_info['f_name'],
        l_name = guest_info['l_name'],
        email = guest_info.get('email'),
        phone = guest_info.get('phone'),
        is_rsvp = guest_info.get('is_rsvp'),
        user_id = get_jwt_identity()
    )

    db.session.add(guest)
    db.session.commit()

    return GuestSchema().dump(guest), 201


# Update a guest
@guests_bp.route('/<int:guest_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_guest(guest_id):
    stmt = db.select(Guest).filter_by(id=guest_id)
    guest = db.session.scalar(stmt)
    guest_info = GuestSchema().load(request.json)
    if guest:
        admin_or_owner_required(guest.user.id)
        guest.f_name = guest_info.get('f_name', guest.f_name)
        guest.l_name = guest_info.get('l_name', guest.l_name)
        guest.email = guest_info.get('email', guest.email)
        guest.phone = guest_info.get('phone', guest.phone)
        guest.is_rsvp = guest_info.get('is_rsvp', guest.is_rsvp)
        db.session.commit()
        return GuestSchema().dump(guest)
    else:
       return {'error': 'Guest not found'}, 404


# Delete a guest
@guests_bp.route('/<int:guest_id>', methods=['DELETE'])
@jwt_required()
def delete_guest(guest_id):
    stmt = db.select(Guest).filter_by(id=guest_id)
    guest = db.session.scalar(stmt)
    if guest:
       admin_or_owner_required(guest.user.id)
       db.session.delete(guest)
       db.session.commit()
       return{}, 200
    else:
       return {'error': 'Guest not found'}, 404
