from pony.orm import PrimaryKey, Required, Set, Optional
from db.db_config import db


class Curso(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    carga_horaria = Optional(float)
    alunos = Set('Aluno')

    @staticmethod
    def amostra_cursos():
        return [
            Curso(nome='Python', carga_horaria=36),
            Curso(nome='Java', carga_horaria=120),
            Curso(nome='JavaScript', carga_horaria=48),
            Curso(nome='GoLang', carga_horaria=72),
        ]
