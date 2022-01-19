from app.modules import BaseModel
from app.extensions import db
from flask import Blueprint

entrega_api = Blueprint('entrega_api', __name__)

class Entrega(BaseModel):
    _tablename__ = 'entregas'

    id = db.Column(db.Interger, primary_key = True, autoincrement = True)
    pedidos = db.relationship('StatusEntrega')

class carrinhodecompras(BaseModel):
    __tablename__= 'Carrinho de Compras'
    id = db.Column(db.Interger, primaryKey=True, autoincrement=True)
    entrega_id = db.Column(db.ForeignKey('entrega.id'))
    carros_id = db.Column(db.ForeignKey('carros.id'))
    motos_id = db.Column(db.ForeignKey('Motos.id'))
    preco = db.column(sum(db.select(carros_id/'preco'),db.select(motos_id/'preco')))
    entregou = db.Column(db.boolean, default = False)

    carros = db.relationship('carros')
    motos = db.relationship('motos')
    
    def json(self):{
        "entrega":self.entrega_id,
        "carro":self.carros_id,
        "moto":self.motos_id,
        "valor":self.preco,
        "entregou":self.entregou
    }
