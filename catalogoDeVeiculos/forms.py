from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, NumberRange
from catalogoDeVeiculos.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")


class FormCadastroUsuario(FlaskForm):
    username = StringField("Nome de usuário:", validators=[DataRequired()])
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("Confirmação de Senha:", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Cadastrar")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado. Faça login para continuar.")


class FormCadastroVeiculo(FlaskForm):
    nome = StringField("Nome: ", validators=[DataRequired()])
    marca = StringField("Marca:", validators=[DataRequired()])
    modelo = StringField("Modelo:", validators=[DataRequired()])
    ano = StringField("Ano:", validators=[DataRequired()])
    cor = StringField("Cor:", validators=[DataRequired()])
    preco = IntegerField("Preço:", validators=[
        DataRequired(),
        NumberRange(min=0, message="O preço deve ser um número inteiro positivo.")
    ])
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Cadastrar")


