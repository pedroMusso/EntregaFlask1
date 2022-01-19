from distutils.command.config import config
from flask import Flask
from .Config import Config
from .extensions import db, migrate
from app.entrega.models import entrega_api
from app.pedidos.models import Carros_api, Motos_api
from app.user.models import user_api

def creat_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(entrega_api)
    app.register_blueprint(Carros_api)
    app.register_blueprint(Motos_api)
    app.register_blueprint(user_api)

    return app
