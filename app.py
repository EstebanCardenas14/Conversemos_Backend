from flask import Flask
from routes.user_routes import user_routes
from dotenv import load_dotenv


# Carga las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.register_blueprint(user_routes)
#cors 
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    return response

@app.route('/')

def index() :
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)