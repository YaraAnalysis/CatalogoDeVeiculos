# cria as rotas do site (links)
from flask import render_template, url_for, redirect
from catalogoDeVeiculos import app, database, bcrypt
from flask_login import login_required, login_user, logout_user
from catalogoDeVeiculos.forms import FormLogin, FormCadastroUsuario
from catalogoDeVeiculos.models import Usuario


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    formlogin = FormLogin()
    return render_template("login.html", form=formlogin)

@app.route("/cadastroUsuario", methods=["GET", "POST"])
def cadastro():
    formCadastroUsuario = FormCadastroUsuario()
    if formCadastroUsuario.validate_on_submit():
        senha = bcrypt.generate_password_hash(formCadastroUsuario.senha.data)
        usuario = Usuario(username=formCadastroUsuario.username.data,
                          email=formCadastroUsuario.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("catalogo", usuario=usuario.username))
    return render_template("cadastroUsuario.html", form=formCadastroUsuario)

@app.route("/editarCatalogo/<usuario>")
@login_required
def catalogo(usuario):
    return render_template("editarCatalogo.html", usuario=usuario)