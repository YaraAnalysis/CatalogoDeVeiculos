from catalogoDeVeiculos import database

class Usuario(database.Model):
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
