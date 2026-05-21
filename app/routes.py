from app import app
from flask import render_template, redirect, url_for
from app.forms import alunoForm
from app.controllerAluno import AlunoController

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = alunoForm()
    if form.validate_on_submit():
        AlunoController.adicionarAluno(
            form.nome.data, form.email.data, form.idade.data,
            form.sexo.data, form.matricula.data, form.cpf.data
        )
        return redirect(url_for('listagem'))
    return render_template('cadastro.html', form = form)


@app.route('/alunos')
def listagem():
    alunos = AlunoController.listar()
    return render_template('alunos.html', alunos=alunos)