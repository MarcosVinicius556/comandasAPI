#Classe de repositório, responsável pelas operações no banco de dados

#Classe modelo de objeto para a aplicação
from models.Funcionario import FuncionarioModel;

#Classe modelo ORM para o banco de dados
from entities.FuncionarioEntity import FuncionarioDB;

#Classe responsável por fornecer a conexão com o banco de dados
import config.database.DatabaseConnection as DatabaseConnection;

def insert(newFuncionario: FuncionarioModel):
    try:
        session = DatabaseConnection.Session();
        
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
        session = DatabaseConnection.Session();
        
        funcionarios = session.query(FuncionarioDB).all();
        return funcionarios;
    except Exception as e:
        raise e; #Criar exceções personalizadas....
    finally:
        session.close();
        
def findById(id: int):
    try:
        session = DatabaseConnection.Session();
        
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one();
        return funcionario;
    except Exception as e:
        raise e;
    finally:
        session.close();
        
def update(newFuncionario: FuncionarioModel):
    try:
        session = DatabaseConnection.Session();
        
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
        session = DatabaseConnection.Session();
        
        session.begin();
        session.delete(funcionario);
        session.commit();
    except Exception as e:
        session.rollback();
        raise e;
    finally:
        session.close();
        
def findByCPF(cpf: str):
    try:
        session = DatabaseConnection.Session();
        
        funcionarios = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == cpf).all();
        return funcionarios;
    except Exception as e:
        raise e;
    finally:
        session.close();
        
def findByCPFAndSenha(cpf: str, senha: str):
    try:
        session = DatabaseConnection.Session();
        
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == cpf).filter(FuncionarioDB.senha == senha).one();
        return funcionario;
    except Exception as e:
        raise e;
    finally:
        session.close();
