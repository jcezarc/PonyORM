from fastapi import APIRouter
from pony.orm import db_session, select
from model.curso import Curso

router = APIRouter()


@router.get('/curso/{nome_curso}', tags=['Curso'])
@db_session
def alunos_por_curso(nome_curso: str):
    query = select(c for c in Curso if c.nome == nome_curso)
    return {
        'curso': nome_curso,
        'alunos': [a.nome for c in query for a in c.alunos]
    }
