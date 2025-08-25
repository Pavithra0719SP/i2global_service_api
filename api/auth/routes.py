from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from marshmallow import  ValidationError
from .service import register_user, authenticate_user
from .model import UserRigisterSchema, UserLoginSchema

api_bp = Blueprint('auth', __name__)

rigiserSchema = UserRigisterSchema()
loginSchema = UserLoginSchema()

@api_bp.route('/register', methods=['POST'])
# @jwt_required()

def register():
    try:
        data = rigiserSchema.load(request.json)
        # current_user = get_jwt_identity()
    except ValidationError as err:
        return jsonify(err.messages), 400
    response, status_code = register_user(data['user_email'], data['password'], data['user_name'])
    return jsonify(response), status_code

@api_bp.route('/login', methods=['POST'])
def login():
    try:
        data = loginSchema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    response, status_code = authenticate_user(data['user_email'], data['password'])
    return jsonify(response), status_code