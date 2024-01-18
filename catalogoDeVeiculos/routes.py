# cria as rotas do site (links)
from flask import render_template, url_for
from catalogoDeVeiculos import app
from flask_login import login_required
from catalogoDeVeiculos.forms import FormLogin, FormCadastroUsuario


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    formlogin = FormLogin()
    return render_template("login.html", form=formlogin)

@app.route("/cadastroUsuario", methods=["GET", "POST"])
def cadastro():
    formCaddastroUsuario = FormCadastroUsuario()
    return render_template("cadastroUsuario.html", form=formCaddastroUsuario)

@app.route("/editarCatalogo/<usuario>")
@login_required
def catalogo(usuario):
    return render_template("editarCatalogo.html", usuario=usuario)