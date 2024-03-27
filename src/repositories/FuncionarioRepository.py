#Classe de repositório, responsável pelas operações no banco de dados

#Classe modelo de objeto para a aplicação
from models.Funcionario import FuncionarioModel;

#Classe modelo ORM para o banco de dados
from entities.FuncionarioModel import FuncionarioDB;

#Classe responsável por fornecer a conexão com o banco de dados
import db;

def insert(newFuncionario: FuncionarioModel):
    try:
        session = db.Session();
        
        obj = FuncionarioDB(None, newFuncionario.nome, newFuncionario.matricula, newFuncionario.cpf, newFuncionario.telefone, newFuncionario.grupo, newFuncionario.senha);
        
        session.begin();
        session.add(obj);
        session.commit();
        
    except Exception as e:
        session.rollback(); 
        raise e; #Criar exceções personalizadas....
    finally:
        session.close();
        
def findAll():
    try:
        session = db.Session();
        
        funcionarios = session.query(FuncionarioDB).all();
        return funcionarios;
    except Exception as e:
        raise e; #Criar exceções personalizadas....
    finally:
        session.close();
        
def findById(id: int):
    try:
        session = db.Session();
        
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one();
        return funcionario;
    except Exception as e:
        raise e;
    finally:
        session.close();
        
def update(newFuncionario: FuncionarioModel):
    try:
        session = db.Session();
        
        session.begin();
        session.add(newFuncionario);
        session.commit();
    except Exception as e:
        session.rollback();
        raise e;
    finally:
        session.close();

def delete(funcionario: FuncionarioDB):
    try:
        session = db.Session();
        
        session.begin();
        session.delete(funcionario);
        session.commit();
    except Exception as e:
        session.rollback();
        raise e;
    finally:
        session.close();
