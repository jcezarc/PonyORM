from pony.orm import Database, db_session, commit, select

db = Database()
db.bind(
    provider='sqlite',
    filename='c:/users/julio/fastapi_pony/db/escola.db',
    create_db=True
)

@db_session
def grava_dados_iniciais(Aluno, Curso):
    if select(c for c in Curso).count() == 0:
        cursos = Curso.amostra_cursos()
        alunos = Aluno.amostra_alunos(cursos)
        commit()
