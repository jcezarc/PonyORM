from fastapi import APIRouter
from pony.orm import db_session, select, count
from model.aluno import Aluno

router = APIRouter()


@router.get('/aluno', tags=['Aluno'])
@db_session
def cursos_por_aluno():
    return select(
        (a.nome, count())
        for a in Aluno for c in a.cursos
    )[:]
