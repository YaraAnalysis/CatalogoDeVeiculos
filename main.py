from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)