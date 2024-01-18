from catalogoDeVeiculos import database, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

class Veiculo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    marca = database.Column(database.String, nullable=False)
    modelo = database.Column(database.String, nullable=False)
    ano = database.Column(database.String, nullable=False)
    cor = database.Column(database.String, nullable=False)
    preco = database.Column(database.Integer, nullable=False)
    foto = database.Column(database.String, default="default.png")
