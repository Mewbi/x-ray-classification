from flask import Blueprint, jsonify, request
from models.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/login', methods=['POST'])
def login():
    
    return jsonify({'image': 'login'}), 200


@user_bp.route('/', methods=['POST'])
def create_user():
    
    return jsonify({'image': 'login'}), 200
