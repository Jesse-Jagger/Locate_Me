from flask import Blueprint, request, jsonify
from models import Marker, db

map_bp = Blueprint('map', __name__)

@map_bp.route('/markers', methods=['GET', 'POST'])
def handle_markers():
    if request.method == 'POST':
        data = request.get_json()
        new_marker = Marker(lat=data['lat'], lng=data['lng'], title=data['title'], description=data['description'])
        db.session.add(new_marker)
        db.session.commit()
        return jsonify({'message': 'Marker added successfully'}), 201
    else:
        markers = Marker.query.all()
        return jsonify([marker.as_dict() for marker in markers])

@map_bp.route('/markers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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