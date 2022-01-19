from app.pedidos.models import carros, motos
from app.modules import BaseModel
from app.extensions import db
from flask import Blueprint

user_api = Blueprint('user_api', __name__)

class User(BaseModel):

    __tablename__ = 'user'

    id = db.Column(db.Interger, primary_key = True, autoincrement = True)
    cpf = db.Column (db.String(15), nullable = False)
    name = db.Column(db.String(70))
    email = db.Column(db.session(70), unique = True, index = True)
    telefone = db.Column(db.String(11), unique = True)
    
    Pedidos = db.relationship('carros','motos')

    def json(self):
        return {
            "cpf": self.cpf,
            "name": self.name,
            "email":self.email,
            "telefone":self.telefone
        }