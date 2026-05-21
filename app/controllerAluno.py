from app.models import Estudante

class AlunoController:
    alunos = []


    @classmethod
    def adicionarAluno(cls, nome, email, idade, sexo, matricula, cpf):
        aluno_novo = Estudante(nome, email, idade, sexo, matricula, cpf)
        cls.alunos.append(aluno_novo)

    @classmethod
    def listar(cls):
        return cls.alunos
    



