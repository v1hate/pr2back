from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# Configuración de CORS para permitir el acceso desde el front-end
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Cambia esto por tu URL de producción

from app import routes, models
