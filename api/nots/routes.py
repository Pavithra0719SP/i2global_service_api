from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from marshmallow import  ValidationError
from .service import create_note, get_notes_by_user, update_note, delete_note, get_note_by_id
from .model import NotsSchema

api_bp = Blueprint('nots', __name__)



@api_bp.route('/notes/create', methods=['POST'])
@jwt_required()

def create():
    try:
        data = NotsSchema().load(request.json)
        current_user = get_jwt_identity()
    except ValidationError as err:
        return jsonify(err.messages), 400
    response, status_code = create_note(data['note_title'], data['note_content'], current_user)
    return jsonify(response), status_code

@api_bp.route('/getall/notes', methods=['GET'])
@jwt_required() 
def get_notes():
    current_user = get_jwt_identity()
    response, status_code = get_notes_by_user(current_user)
    return jsonify(response), status_code

@api_bp.route('/notes/getbyid/<note_id>', methods=['GET'])
@jwt_required() 
def get_note(note_id):
    current_user = get_jwt_identity()
    response, status_code = get_note_by_id(note_id, current_user)
    return jsonify(response), status_code

@api_bp.route('/notes/update/<note_id>', methods=['PUT'])
@jwt_required()
def update(note_id):
    try:
        data = NotsSchema().load(request.json)
        current_user = get_jwt_identity()
    except ValidationError as err:
        return jsonify(err.messages), 400
    response, status_code = update_note(note_id, data['note_title'], data['note_content'], current_user)
    return jsonify(response), status_code

@api_bp.route('/notes/delete/<note_id>', methods=['DELETE'])
@jwt_required() 
def delete(note_id):
    current_user = get_jwt_identity()
    response, status_code = delete_note(note_id, current_user)
    return jsonify(response), status_code

