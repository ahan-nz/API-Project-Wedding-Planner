from flask import Blueprint, request
from init import db
from models.wedding import Wedding, WeddingSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_or_owner_required

weddings_bp = Blueprint('weddings', __name__, url_prefix='/weddings')


# Get all weddings
@weddings_bp.route('/')
# @ jwt required
def all_weddings():
    # @ Admin required
    stmt = db.select(Wedding)
    weddings = db.session.scalars(stmt).all()
    return WeddingSchema(many=True).dump(weddings)


# Get one wedding
@weddings_bp.route('/<int:wedding_id>')
# @ jwt required
def one_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id)
    wedding = db.session.scalar(stmt)
    if wedding:
        # @ Admin or owner required
        return WeddingSchema().dump(wedding)
    else:
        return {'error': 'Wedding entry not found'}, 404
    

# Create a new wedding
@weddings_bp.route('/', methods=['POST'])
# @ jwt required
def create_wedding():
    wedding_info = WeddingSchema().load(request.json)

    wedding = Wedding(
        date_of_wedding = wedding_info['date_of_wedding'],
        user_id = get_jwt_identity()
    )

    db.session.add(wedding)
    db.session.commit()

    return WeddingSchema().dump(wedding), 201


# Update a wedding
@weddings_bp.route('/<int:wedding_id>', methods=['PUT', 'PATCH'])
# @ jwt required
def update_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id).first()
    wedding = db.session.scalar(stmt)
    wedding_info = WeddingSchema().load(request.json)
    if wedding:
        # @admin or owner required
        wedding.date_of_wedding = wedding_info.get('date_of_wedding', wedding.date_of_wedding)
        db.session.commit()
        return WeddingSchema().dump(wedding)
    else:
       return {'error': 'Wedding entry not found'}, 404


# Delete a wedding
@weddings_bp.route('/<int:wedding_id>', methods=['DELETE'])
# @ jwt required
def delete_wedding(wedding_id):
    stmt = db.select(Wedding).filter_by(id=wedding_id)
    wedding = db.session.scalar(stmt)
    if wedding:
       # @ admin or owner required
       db.session.delete(wedding)
       db.session.commit()
       return{}, 200
    else:
       return {'error': 'Wedding entry not found'}, 404