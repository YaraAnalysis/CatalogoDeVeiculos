from flask import Flask, render_template

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

@app.route("/editarCatalogo")
def catalogo():
    return render_template("editarCatalogo.html")

if __name__ == "__main__":
    app.run(debug=True)