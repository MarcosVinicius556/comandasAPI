from fastapi import APIRouter;
from mod_funcionario.Funcionario import FuncionarioModel;
from mod_funcionario.FuncionarioDB import FuncionarioDB;
import db;

from fastapi import Depends
from security import get_current_active_user;

#Objeto para criação das rotas
router = APIRouter(dependencies=[Depends(get_current_active_user)]);

@router.post("/funcionario/", tags=["Funcionário"])
def create(obj: FuncionarioModel):
    try:
        session = db.Session();
        
        obj = FuncionarioDB(None, obj.nome, obj.matricula, obj.cpf, obj.telefone, obj.grupo, obj.senha);
        
        session.begin();
        session.add(obj);
        session.commit();
        
    except Exception as e:
        print(e)
        session.rollback(); 
        return {"erro": str(e)}, 400
    finally:
        session.close();
    return { "id": obj.id_funcionario }, 200;

@router.get("/funcionario/", tags=["Funcionário"])
def findAll():
    try:
        session = db.Session();
        
        funcionarios = session.query(FuncionarioDB).all();
        return funcionarios, 200;
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.get("/funcionario/{id}", tags=["Funcionário"])
def findById(id: int):
    try:
        session = db.Session();
        
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one();
        return funcionario, 200;
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.put("/funcionario/{id}", tags=["Funcionário"])
def update(id: int, obj: FuncionarioModel):
    try:
        session = db.Session();
        session.begin();
        
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one();
        
        if funcionario is None:
            return {"Detail": "Nenhum registro encontrado!"}, 400;
        
        funcionario.nome = obj.nome;
        funcionario.matricula = obj.matricula;
        funcionario.cpf = obj.cpf;
        funcionario.telefone = obj.telefone;
        funcionario.grupo = obj.grupo;
        funcionario.senha = obj.senha;
        
        # session.add(obj);
        
        session.commit();
        
        return {"Detail": "Funcionário atualizado com sucesso!"}, 200;
    except Exception as e:
        session.rollback();
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete(id: int):
    try:
        session = db.Session();
        session.begin();
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one();

        if funcionario is None:
            return {"Detail": "Nenhum registro encontrado!"}, 400;
        
        session.delete(funcionario);
        session.commit();
            
        return { "detail": "Funcionário removido com sucesso!" }, 200;

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close();

@router.get("/funcionario/cpf/{cpf}", tags=["Funcionário - Valida CPF"])
def findByCPF(cpf: str):
    try:
        session = db.Session();
        
        funcionarios = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == cpf).all();
        return funcionarios, 200;
    except Exception as e:
        session.rollback();
        return {"Error: ": str(e) }, 400
    finally:
        session.close();

# @router.post("/funcionario/login", tags=["Funcionário - Login"])
# def findByCPFAndSenha(obj: dict["cpf": str, "senha": str]):
#     try:
#         session = db.Session();
#         funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == obj["cpf"]).filter(FuncionarioDB.senha == obj["senha"]).first();
        
#         return funcionario, 200;
#     except Exception as e:
#         return {"Error: ": str(e)}, 400
#     finally:
#         session.close();
