import ast
import re
from services.user_services import UserService
from services.auth_services import AuthService

class UserController:
    # Inicializamos los servicios de base de datos y de autenticación
    def __init__(self):
        self.db_service = UserService()
        self.auth_service = AuthService()
    
    # Método para iniciar sesión y obtener el token
    def login(self, email, password):
        try :
            auth = self.auth_service.login(email, password)
            return auth['idToken']
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return None
    
    # Método para crear un usuario y obtener el token
    def create_user(self, user):
        try:
            user_created = self.auth_service.createUser(user['email'], user['password'])
            if user_created:
                #agregar el UID de firebase al usuario
                user['uid'] = user_created.uid
                self.db_service.insert_one(user)
                auth = self.auth_service.login(user['email'], user['password'])
                return auth['idToken']
            else:
                return 'Error creating user'
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return 'Error creating user'

    # Método para obtener un usuario por su ID
    def get_user(self, user_id):
        user = self.db_service.find_one({'uid': user_id})
        user = str(user)
        #Reemplazar ObjectId con una cadena vacía
        cleaned_string = re.sub(r"ObjectId\('[a-f\d]{24}'\)", "''", user)
        # Convertir la cadena en un diccionario Python
        parsed_object = ast.literal_eval(cleaned_string)
        #eliminar el campo _id
        del parsed_object['_id']
        return parsed_object
    
    # Método para editar un usuario por su ID
    def update_user(self, user_id, user):
        self.db_service.update_one({'uid': user_id}, user)
        user = self.db_service.find_one({'uid': user_id})
        user = str(user)
        #Reemplazar ObjectId con una cadena vacía
        cleaned_string = re.sub(r"ObjectId\('[a-f\d]{24}'\)", "''", user)
        # Convertir la cadena en un diccionario Python
        parsed_object = ast.literal_eval(cleaned_string)
        #eliminar el campo _id
        del parsed_object['_id']
        return parsed_object



    def get_users(self):
        users = self.db_service.find({})
        return str([user for user in users])

    def delete_user(self, user_id):
        self.db_service.delete_one({'_id': user_id})
        return 'User deleted successfully'

    def authenticate_token(self, token):
        response = self.auth_service.authenticateToken(token)
        return response
    
