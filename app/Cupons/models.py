from app.modules import BaseModel
from extensions import db

class cuponsdedesconto(BaseModel):
    __tablename__ = 'CuponsdeDesconto'

    id = db.Column(db.Interger, primaryKey = True, autoincrement=True)
    nome = db.Column(db.session(25))
    usuario = db.column(db.ForeignKey('user.id'))