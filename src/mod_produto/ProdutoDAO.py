from fastapi import APIRouter;

from mod_produto.Produto import ProdutoModel;

#Objeto para criação das rotas
router = APIRouter();

#Definição das rotas
@router.get("/produto/", tags=["Produto"])
def get_produto():
    return { "msg": "GET todos executado" }, 200;

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    return { "msg": "GET um executado" }, 200;

@router.post("/produto/", tags=["Produto"])
def post_produto(f: ProdutoModel):
    return { "msg": "POST executado", "nome": f.nome, "descrição": f.descricao, "valor_unitario": f.valor_unitario }, 200;

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, f: ProdutoModel):
    return { "msg": "PUT executado", "id": id, "nome": f.nome, "descrição": f.descricao, "valor_unitario": f.valor_unitario }, 201;

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return { "msg": "DELETE executado" }, 201;


