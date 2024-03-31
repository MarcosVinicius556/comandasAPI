from fastapi import APIRouter;
from models.Produto import ProdutoModel;

from services import ProdutoService as service;

#Objeto para criação das rotas
router = APIRouter();

@router.post("/produto/", tags=["Produto"])
def create(obj: ProdutoModel):
    newProduto = service.insert(obj);
    return { "id": newProduto.id_produto }, 200;

@router.get("/produto/", tags=["Produto"])
def findAll():
    produtos = service.findAll();
    return produtos, 200;

@router.get("/produto/{id}", tags=["Produto"])
def findById(id: int):
    produto = service.findById(id);
    return produto, 200;

@router.put("/produto/{id}", tags=["Produto"])
def update(id: int, obj: ProdutoModel):
    updatedProduto = service.update(id, obj);
    return { "id": updatedProduto.id_produto }, 200;

@router.delete("/produto/{id}", tags=["Produto"])
def delete(id: int):
    service.delete(id);
    return { "detail": "Produto removido com sucesso!" }, 200;

