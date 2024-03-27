from fastapi import APIRouter;
from mod_funcionario.Funcionario import FuncionarioModel;

#Import das classes de persistência
import db;
from mod_funcionario.FuncionarioModel import FuncionarioDB;

#Objeto para criação das rotas
router = APIRouter();

#Definição das rotas
@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    try:
        session = db.Session();
        
        #Busca todos os registros
        dados = session.query(FuncionarioDB).all();
        return dados, 200;
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close(); #Garante que sempre ao final de uma execução irá finalizar a sessão

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    try: 
        session = db.Session();
        
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).all();
        
        return dados, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;
    finally:
        session.close(); 

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(obj: FuncionarioModel):
    try:
        session = db.Session();
        #Criando o obj que será persistido através das informações recebidas
        newFuncionario = FuncionarioDB(None, obj.nome, obj.matricula, obj.cpf, obj.telefone, obj.grupo, obj.senha);
        
        #Abrindo uma transação e logo após fechando-a
        session.begin();
        session.add(newFuncionario);
        session.commit();
        
        return { "id": obj.id_funcionario }, 200;
    except Exception as e:
        session.rollback(); #Caso dê algum tipo de erro irá realizar o rollback da transação
        return {"erro": str(e)}, 400;
    finally:
        session.close();

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, obj: FuncionarioModel):
    try:
        session = db.Session();
        
        #Aqui buscamos o funcionário de acordo com seu id
        updatedFuncionario = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one();
        
        #E após atualizamos as informações dele para persistir no banco
        updatedFuncionario.nome = obj.nome;
        updatedFuncionario.matricula = obj.matricula;
        updatedFuncionario.cpf = obj.cpf;
        updatedFuncionario.telefone = obj.telefone;
        updatedFuncionario.grupo = obj.grupo;
        updatedFuncionario.senha = obj.senha;
        
        session.begin();
        session.add(updatedFuncionario);
        session.commit();
        
        return { "id": id }, 200;
    except Exception as e:
        session.rollback();
        return { "erro": str(e) }, 400;
    finally:
        session.close();

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        session = db.Session();
        
        #Localizamos o funcionario a ser removido
        funcionarioToRemove = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one();
        
        #Abrimos uma transação e o removemos do banco
        session.begin();
        session.remove(funcionarioToRemove);
        session.commit();
        
    except Exception as e:
        session.rollback();
        return {"erro": str(e)}, 400
    finally:
        session.close();
    
@router.post("/funcionario/login", tags=["Funcionário - Login"])
def login_funcionario(obj: FuncionarioModel):
    try:
        session = db.Session();
        
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == obj.cpf).filter(FuncionarioDB.senha == obj.senha).one();
        
        return funcionario, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;
    finally:
        session.close();

@router.get("/funcionario/cpf/{cpf}", tags=["Funcionário - Valida CPF"])
def cpf_funcionario(cpf: str):
    try:
        session = db.Session();
        
        funcionarios = session.query().filter(FuncionarioDB.cpf == cpf).all();
        
        return funcionarios, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;
    finally:
        session.close();