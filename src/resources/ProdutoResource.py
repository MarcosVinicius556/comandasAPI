from fastapi import APIRouter;
from models.Produto import ProdutoModel;

from services import ProdutoService as service;

#Objeto para criação das rotas
router = APIRouter();

@router.post("/produto/", tags=["Produto"])
def create(obj: ProdutoModel):
    try:
        newProduto = service.insert(obj);
        
        return { "id": newProduto.id_produto }, 200;
    except Exception as e:
        return {"erro": str(e)}, 400; #Criar um exceptionHandler

@router.get("/produto/", tags=["Produto"])
def findAll():
    try:
        produtos = service.findAll();
        return produtos, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;  #Criar um exceptionHandler

@router.get("/produto/{id}", tags=["Produto"])
def findById(id: int):
    try: 
        produto = service.findById(id);
        
        return produto, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;

@router.put("/produto/{id}", tags=["Produto"])
def update(id: int, obj: ProdutoModel):
    try:
        updatedProduto = service.update(id, obj);
        
        return { "id": updatedProduto.id_produto }, 200;
    except Exception as e:
        return { "erro": str(e) }, 400;

@router.delete("/produto/{id}", tags=["Produto"])
def delete(id: int):
    try:
        service.delete(id);
    except Exception as e:
        return {"erro": str(e)}, 400

