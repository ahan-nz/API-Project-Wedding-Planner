from flask import Blueprint, request
from init import db
from models.wedding import Wedding, WeddingSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required, admin_or_owner_required

weddings_bp = Blueprint('weddings', __name__, url_prefix='/weddings')


# Get all weddings
@weddings_bp.route('/')
@jwt_required()
def all_weddings():
    admin_required()
    stmt = db.select(Wedding)
    weddings = db.session.scalars(stmt).all()
    return WeddingSchema(many=True, exclude=['venue_id']).dump(weddings)


# Get one wedding
@weddings_bp.route('/<int:wedding_id>')
@jwt_required()
def one_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id)
    wedding = db.session.scalar(stmt)
    if wedding:
        admin_or_owner_required(wedding.user.id)
        return WeddingSchema(exclude=['id', 'venue_id']).dump(wedding)
    else:
        return {'error': 'Wedding entry not found'}, 404
    

# Create a new wedding
@weddings_bp.route('/', methods=['POST'])
@jwt_required()
def create_wedding():
    wedding_info = WeddingSchema().load(request.json)

    wedding = Wedding(
        date_of_wedding = wedding_info['date_of_wedding'],
        user_id = get_jwt_identity(),
        venue_id = wedding_info['venue_id']
    )

    db.session.add(wedding)
    db.session.commit()

    return WeddingSchema(exclude=['venue_id']).dump(wedding), 201


# Update a wedding
@weddings_bp.route('/<int:wedding_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id)
    wedding = db.session.scalar(stmt)
    wedding_info = WeddingSchema().load(request.json)
    if wedding:
        admin_or_owner_required(wedding.user.id)
        wedding.date_of_wedding = wedding_info.get('date_of_wedding', wedding.date_of_wedding)
        wedding.venue_id = wedding_info.get('venue_id', wedding.venue_id)
        db.session.commit()
        return WeddingSchema(exclude=['venue_id']).dump(wedding)
    else:
       return {'error': 'Wedding entry not found'}, 404


# Delete a wedding
@weddings_bp.route('/<int:wedding_id>', methods=['DELETE'])
@jwt_required()
def delete_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id)
    wedding = db.session.scalar(stmt)
    if wedding:
       admin_or_owner_required(wedding.user.id)
       db.session.delete(wedding)
       db.session.commit()
       return{}, 200
    else:
       return {'error': 'Wedding entry not found'}, 404