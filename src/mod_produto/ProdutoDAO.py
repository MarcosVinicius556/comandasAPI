from fastapi import APIRouter;
from mod_produto.Produto import ProdutoModel;
from mod_produto.ProdutoDB import ProdutoDB;
import db;

from fastapi import Depends
from security import get_current_active_user;

#Objeto para criação das rotas
router = APIRouter(dependencies=[Depends(get_current_active_user)]);

@router.post("/produto/", tags=["Produto"])
def create(obj: ProdutoModel):
    try:
        session = db.Session();
        
        obj = ProdutoDB(None, obj.nome, obj.descricao, obj.foto, obj.valor_unitario);
        
        session.begin();
        session.add(obj);
        session.commit();
        
    except Exception as e:
        session.rollback(); 
        return {"erro": str(e)}, 400
    finally:
        session.close();
    return { "id": obj.id_produto }, 200;

@router.get("/produto/", tags=["Produto"])
def findAll():
    try:
        session = db.Session();
        
        produtos = session.query(ProdutoDB).all();
        return produtos, 200;
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.get("/produto/{id}", tags=["Produto"])
def findById(id: int):
    try:
        session = db.Session();
        
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one();
        return produto, 200;
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.put("/produto/{id}", tags=["Produto"])
def update(id: int, obj: ProdutoModel):
    try:
        session = db.Session();
        
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one();
        
        if produto is None:
            return {"Detail": "Nenhum registro encontrado!"}, 400;
        
        produto.nome = obj.nome;
        produto.descricao = obj.descricao;
        produto.foto = obj.foto;
        produto.valor_unitario = obj.valor_unitario;
        
        session.begin();
        session.add(obj);
        session.commit();
        
        return {"detail": "Produto atualizado com sucesso!"}, 200
    except Exception as e:
        session.rollback();
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.delete("/produto/{id}", tags=["Produto"])
def delete(id: int):
    try:
        session = db.Session();
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one();

        if produto is None:
            return {"Detail": "Nenhum registro encontrado!"}, 400;
        
        session.begin();
        session.delete(produto);
        session.commit();
            
        return { "detail": "Produto removido com sucesso!" }, 200;

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

