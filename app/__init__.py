from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-secreta-123'

from app.routes import homepage, sobre, contato, cadastro, listagem