from fastapi import APIRouter;
from mod_cliente.Cliente import ClienteModel;
from mod_cliente.ClienteDB import ClienteDB;
import db;

from fastapi import Depends
from security import get_current_active_user;

#Objeto para criação das rotas
router = APIRouter(dependencies=[Depends(get_current_active_user)]);

@router.post("/cliente/", tags=["Cliente"])
def create(obj: ClienteModel):
    try:
        session = db.Session();
        
        obj = ClienteDB(None, obj.nome, obj.cpf, obj.telefone);
        
        session.begin();
        session.add(obj);
        session.commit();
        
    except Exception as e:
        session.rollback(); 
        return {"erro": str(e)}, 400
    finally:
        session.close();
    return { "id": obj.id_cliente }, 200;

@router.get("/cliente/", tags=["Cliente"])
def findAll():
    try:
        session = db.Session();
        
        clientes = session.query(ClienteDB).all();
        return clientes, 200;
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.get("/cliente/{id}", tags=["Cliente"])
def findById(id: int):
    try:
        session = db.Session();
        
        cliente = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one();
        return cliente, 200;
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.put("/cliente/{id}", tags=["Cliente"])
def update(id: int, obj: ClienteModel):
    try:
        session = db.Session();
        
        cliente = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one();
        
        if cliente is None:
            return {"Detail": "Nenhum registro encontrado!"}, 400;
        
        cliente.nome = obj.nome;
        cliente.cpf = obj.cpf;
        cliente.telefone = obj.telefone;
        
        session.begin();
        session.add(obj);
        session.commit();
        
        return {"detail": "Cliente atualizado com sucesso!"}, 200
    except Exception as e:
        session.rollback();
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete(id: int):
    try:
        session = db.Session();
        cliente = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one();

        if cliente is None:
            return {"Detail": "Nenhum registro encontrado!"}, 400;
        
        session.begin();
        session.delete(cliente);
        session.commit();
            
        return { "detail": "Cliente removido com sucesso!" }, 200;

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();
    
    

