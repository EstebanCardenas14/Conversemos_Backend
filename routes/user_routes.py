from flask import Blueprint, request
from controller.user_controller import UserController

user_routes = Blueprint('user_routes', __name__)
user_controller = UserController()

@user_routes.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_users()

@user_routes.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_user(user_id)

@user_routes.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return user_controller.create_user(data)

@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return user_controller.update_user(user_id, data)

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete_user(user_id)
