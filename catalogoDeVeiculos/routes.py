# cria as rotas do site (links)
from flask import render_template, url_for
from catalogoDeVeiculos import app


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastroUsuario")
def cadastro():
    return render_template("cadastroUsuario.html")

@app.route("/editarCatalogo/<usuario>")
def catalogo(usuario):
    return render_template("editarCatalogo.html", usuario=usuario)