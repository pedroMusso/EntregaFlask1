from app.modules import BaseModel
from app.extensions import db
from flask import Blueprint

Carros_api = Blueprint('Carros_api', __name__)
Motos_api = Blueprint('Motos_api', __name__)

class carros(BaseModel):
    __tablename__ = 'Carros'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelo = db.Column(db.String(70))
    ano = db.Column(db.String(4))
    preco = db.Column(db.String(70))
    kilometragem = db.Column(db.String(70))
    cor = db.Column(db.String(70))
    quantidade = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def json(self):
        return {
            "id":self.id,
            "modelo":self.modelo,
            "ano":self.ano,
            "preco":self.preco,
            "kilometragem":self.kilometragem,
            "cor":self.cor,
            "quatidade":self.quantidade
        }

class motos(BaseModel):
    __tablename__ = 'Motos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelo = db.Column(db.String(70))
    ano = db.Column(db.String(4))
    preco = db.Column(db.String(70))
    kilometragem = db.Column(db.String(70))
    cor = db.Column(db.String(70))
    quantidade = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def json(self):
        return {
            "id":self.id,
            "modelo":self.modelo,
            "ano":self.ano,
            "preco":self.preco,
            "kilometragem":self.kilometragem,
            "cor":self.cor,
            "quatidade":self.quantidade
        }

