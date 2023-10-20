from flask import Flask
from routes.user_routes import user_routes
from dotenv import load_dotenv


# Carga las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.register_blueprint(user_routes)

@app.route('/')

def index() :
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)