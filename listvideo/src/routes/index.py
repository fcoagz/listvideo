from flask import Blueprint, jsonify

route = Blueprint('index', __name__)

@route.get('/')
def index():
    return jsonify({'message': 'Welcome to API!'})