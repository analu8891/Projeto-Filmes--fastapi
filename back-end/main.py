from fastapi import FastAPI
import funcao

# Como execultar o Fastapi
# python -m uvicorn main:app --reload

app = FastAPI(title="Gerenciador de filmes")

#Criando a rota 
@app.get("/")
def home():
    return{"mensagem":"Bem-vindo ao gerenciador de filmes"}


@app.post("filmes")
def criar_filmes(titulo: str, genero: str, ano: int, nota: float):
    funcao.cadastrar_filme(titulo, genero, ano, nota)
    return {"mensagem" : "Filme cadatrado com sucesso!"}
    