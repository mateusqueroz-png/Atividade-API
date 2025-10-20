from fastapi import FastAPI, Query

import funcao as f

app = FastAPI(title="gerenciador de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bom dia - Bem vindo ao gerenciador de Produtos"}

@app.get("/Produtos")
def catalogo():
    produto = f.listar_movies()
    lista = []
    for produto in produto:
        lista.append({
            "id": produto[0],
            "avaliação": produto[4]
        })
    return {"Produtos": lista}

@app.post("/produtos ")
def adicionar_produto(titulo: int, nota: float):
    f.criar_produto(titulo, nota)
    return {"mensagem": "produtos adicionado com sucesso"}

@app.put("/produtos/{id_produtos}")
def atualizar_produtos(id_produto: int, nova_avaliacao: float = Query(...)):
    filme = f.buscar_movie(id_produto)
    if filme:
        f.atualizar_movies(id_produto, nova_avaliacao)
        return {"mensagem": "produto atualizado com sucesso"}
    else:
        return {"erro": "produto não encontrado"}

