#Importar herramientas
#Acceder a las herramientas para crear la app web
from flask import flask, request, jsonify 

# Para manipular la BDD

from flask_sqlalchemy import SQLAlchemy

#Módulo cors es para que me parmita accder desde el frontend al backend

from flask_cors import CORS

#crear la app  

app = Flask(__name__)

# Para que permita acceder desde el fronted al backend
CORS(app)

#Para configurar a la app la BDD

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@localhost:3306/flask_api' #'mysql+pymysql://usuario:contraseña@localhost:3306/flask_api'
app.config['SQLALCHEMY_-TRACK_MODIFICATIONS']= False


