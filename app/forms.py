from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange


class alunoForm(FlaskForm):
    nome      = StringField('Nome', validators=[DataRequired()])
    email     = StringField('Email', validators=[DataRequired(), Email()])
    idade     = IntegerField('Idade', validators=[DataRequired()])
    sexo      = StringField('Sexo', validators=[DataRequired()])
    matricula = IntegerField('Matrícula', validators=[DataRequired()])
    cpf       = IntegerField('CPF', validators=[DataRequired()])

    submit   = SubmitField('Cadastrar')