
from tkinter import INSERT, ON
from tkinter.tix import COLUMN, Select
from app.modules import BaseModel
from app.pedidos.models import carros,motos
from app.user.models import User
from app.extensions import db
from flask import Blueprint

entrega_api = Blueprint('entrega_api', __name__)

class Entrega(BaseModel):
    __tablename__ = 'entregas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.ForeignKey('user.id'))
    pedidos = db.relationship('Carrinho de Compras')

class carrinhodecompras(BaseModel):
    __tablename__= 'Carrinho de Compras'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entrega_id = db.Column(db.ForeignKey('entregas.id'))
    carros_id = db.Column(db.ForeignKey('Carros.id'))
    motos_id = db.Column(db.ForeignKey('Motos.id'))
    preco = db.Column(db.Integer)
    entregou = db.Column(db.Boolean, default = False)

    carros = db.relationship('carros')
    motos = db.relationship('motos')
    
    def json(self):{
        "entrega":self.entrega_id,
        "carro":self.carros_id,
        "moto":self.motos_id,
        "valor":self.preco,
        "entregou":self.entregou
    }
