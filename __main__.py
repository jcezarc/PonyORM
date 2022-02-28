from fastapi import FastAPI
import uvicorn
from routes import aluno, curso
from db.db_config import db, grava_dados_iniciais
from model.aluno import Aluno
from model.curso import Curso

def create_app():
    db.generate_mapping(create_tables=True)
    grava_dados_iniciais(Aluno, Curso)
    app = FastAPI()
    app.include_router(aluno.router)
    app.include_router(curso.router)
    return app

app = create_app()
uvicorn.run(app)
