from pony.orm import PrimaryKey, Required, Set, Optional
from db.db_config import db
from random import sample

class Aluno(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    email = Optional(str, unique=True)
    cursos = Set('Curso')

    @staticmethod
    def amostra_alunos(cursos: list):
        return [Aluno(nome=n, email=e, cursos=sample(cursos)) for n, e in [
            ('Mirella Campos', 'mirella.campos@wtf.com'),
            ('Luiz Gustavo Alves', 'luiz-gustavo.alves@z2.com'),
            ('Valentina Vieira', 'valentina.vieira@dmz.org'),
            ('Daniel Fogaça', 'daniel.fogaca@porto.net'),
        ]]
