from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from models import User, db, Marker

map_bp = Blueprint('map', __name__)

@map_bp.route('/api/map/markers', methods=['GET', 'POST'])
def handle_markers():
    if request.method == 'POST':
        data = request.get_json()
        new_marker = Marker(
            lat=data['lat'],
            lng=data['lng'],
            title=data['title'],
            description=data['description']
        )
        db.session.add(new_marker)
        db.session.commit()
        return jsonify({'message': 'Marker added successfully'}), 201
    else:
        markers = Marker.query.all()
        return jsonify([marker.as_dict() for marker in markers])

@map_bp.route('/api/map/markers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_marker(id):
    marker = Marker.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(marker.as_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        marker.lat = data['lat']
        marker.lng = data['lng']
        marker.title = data['title']
        marker.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Marker updated successfully'})
    elif request.method == 'DELETE':
        db.session.delete(marker)
        db.session.commit()
        return jsonify({'message': 'Marker deleted successfully'})
    
@auth_bp.route('/api/auth/profile', methods=['GET', 'PUT']) # type: ignore
def profile():
    if request.method == 'GET':
        # Fetch profile details
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user:
            return jsonify({'username': user.username, 'email': user.email}), 200
        else:
            return jsonify({'message': 'User not found'}), 404

    elif request.method == 'PUT':
        # Update profile details
        data = request.get_json()
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user:
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return jsonify({'message': 'Profile updated successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404