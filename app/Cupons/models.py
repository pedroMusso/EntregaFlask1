from app.modules import BaseModel
from app.user.models import User
from extensions import db

class cuponsdedesconto(BaseModel):
    __tablename__ = 'CuponsdeDesconto'

    id = db.Column(db.Integer, primary_Key = True, autoincrement=True)
    nome = db.Column(db.String(25))
    valor = db.Column(db.String(20))
    user_id = db.Collumn(db.Integer, db.ForeignKey('user_id'))
    