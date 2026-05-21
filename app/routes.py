from app import app
from flask import render_template [cite: 55, 56]

@app.route('/')
def homepage():
    return render_template('index.html') [cite: 57, 58, 59]

@app.route('/sobre')
def sobre():
    return render_template('sobre.html') [cite: 107]

@app.route('/contato')
def contato():
    return render_template('contato.html') [cite: 107]