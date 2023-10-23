import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os
from dotenv import load_dotenv
import requests

load_dotenv()

class AuthService : 
    def __init__(self):
        try : 
            service_account_path = os.path.join(os.getcwd(), 'conversemos-firebase-adminsdk.json')
            cred = credentials.Certificate(service_account_path)
            firebase_admin.initialize_app(cred)
            print("Conexión con Firebase exitosa")
        except Exception as e:
            print(f"Error al conectar con Firebase : {e}")
    

    def createUser(self, email, password):
        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            return user
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return None

    def getUser(self, uid):
        try:
            user = auth.get_user(uid)
            return user
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None
    def getUsers(self):
        try:
            users = auth.list_users()
            return users
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return None
  
    def deleteUser(self, uid):
        try:
            auth.delete_user(uid)
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return None

    def authenticateToken (self, token):
        try:
            decoded_token = auth.verify_id_token(token)
            return {
                        'uid': decoded_token['uid'],
                        'email': decoded_token['email'],
                    }
        except Exception as e:
            print(f"Error al autenticar token: {e}")
            return None
    def deleteToken (self, token): 
        try:
            auth.revoke_refresh_tokens(token)
        except Exception as e:
            print(f"Error al eliminar token: {e}")
            return None
    def refreshToken (self, token): 
        try:
            auth.verify_id_token(token, check_revoked=True)
        except Exception as e:
            print(f"Error al refrescar token: {e}")
            return None
    def login(self, email, password):
        try :
            url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=' + os.getenv('FIREBASE_API_KEY')
            headers = {"Content-Type": "application/json"}
            data = '{"email":"' + email+ '","password":"' + password + '","returnSecureToken":true}'
            response = requests.post(url, data=data, headers=headers)
            return response.json()
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return None