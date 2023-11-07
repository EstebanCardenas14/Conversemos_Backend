from functools import wraps
import re
from flask import Blueprint, request, jsonify
from controller.user_controller import UserController
from flask_cors import cross_origin

user_routes = Blueprint('user_routes', __name__)
user_controller = UserController()

# Decorador para verificar el token
def authenticate_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({'message': 'Token no proporcionado'}), 401
        infoUser = user_controller.authenticate_token(token.split(" ")[1])
        if user_controller.authenticate_token(token.split(" ")[1]):
            #mandar infoUser a la función que se llame con el decorador para que sepa que usuario está logueado
            return f(infoUser, *args, **kwargs)
            #return f(*args, **kwargs)
        else:
            return jsonify({'message': 'Token inválido'}), 401
        return f(*args, **kwargs)  # Aquí simplemente pasamos a la función si no hay lógica de autenticación implementada
    return decorated_function


# Rutas de la API
# Ruta para iniciar sesión y obtener el token
@cross_origin
@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if email is not None and password is not None:
        response = user_controller.login(email, password)
        return jsonify({'Token': response}), 200
    else:
        # Manejar el caso en el que los datos no estén presentes en la solicitud
        return jsonify({'message': 'Faltan credenciales de inicio de sesión'}), 400

# Ruta para crear un usuario y obtener el token
@cross_origin
@user_routes.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    response = user_controller.create_user(data)
    return jsonify({'message': 'User created successfully', 'Token' : response }), 200

# Rutas para obtener el usuario logueado
@cross_origin
@user_routes.route('/user', methods=['GET'])
@authenticate_token
def get_user(user_id):
    user = user_controller.get_user(user_id['uid'])
    return jsonify({'usuario': user}), 200#user_controller.get_user(user_id)

# Rutas para editar el usuario logueado
@cross_origin
@user_routes.route('/user', methods=['PUT'])
@authenticate_token
def update_user(user_id):
    data = request.get_json()
    # eliminar atributo uid, email y password si llega en la solicitud 
    if 'uid' in data:
        del data['uid']
    if 'email' in data:
        del data['email']
    if 'password' in data:
        del data['password']
    response = user_controller.update_user(user_id['uid'], data)
    return jsonify({'message': 'User updated successfully', 'user' : response}), 200
