from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Catálogo de Veículos à Venda"

@app.route("/login")
def login():
    return "Login do Usuário"

@app.route("/cadastro")
def cadastro():
    return "Cadastro de Usuário"

@app.route("/catalogo")
def catalogo():
    return "Cadastro de Veículos"

if __name__ == "__main__":
    app.run(debug=True)