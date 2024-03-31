#Classe de repositório, responsável pelas operações no banco de dados

#Classe modelo de objeto para a aplicação
from models.Cliente import ClienteModel;

#Classe modelo ORM para o banco de dados
from entities.ClienteEntity import ClienteDB;

#Classe responsável por fornecer a conexão com o banco de dados
import config.database.DatabaseConnection as DatabaseConnection;

from services.exceptions.DatabaseException import DatabaseException;

def insert(newCliente: ClienteModel):
    try:
        session = DatabaseConnection.Session();
        
        obj = ClienteDB(None, newCliente.nome, newCliente.cpf, newCliente.telefone);
        
        session.begin();
        session.add(obj);
        session.commit();
        
    except Exception as e:
        session.rollback(); 
        raise DatabaseException("Ocorreu um erro ao persistir o objeto.");
    finally:
        session.close();
        
def findAll():
    try:
        session = DatabaseConnection.Session();
        
        clientes = session.query(ClienteDB).all();
        return clientes;
    except Exception as e:
        raise DatabaseException("Ocorreu um erro ao buscar todos os objetos.");
    finally:
        session.close();
        
def findById(id: int):
    try:
        session = DatabaseConnection.Session();
        
        cliente = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one();
        return cliente;
    except Exception as e:
        raise DatabaseException("Ocorreu um erro ao buscar o objeto.");
    finally:
        session.close();
        
def update(newCliente: ClienteModel):
    try:
        session = DatabaseConnection.Session();
        
        session.begin();
        session.add(newCliente);
        session.commit();
    except Exception as e:
        session.rollback();
        raise DatabaseException("Ocorreu um erro ao atualizar o objeto.");
    finally:
        session.close();

def delete(cliente: ClienteModel):
    try:
        session = DatabaseConnection.Session();
        
        session.begin();
        session.delete(cliente);
        session.commit();
    except Exception as e:
        session.rollback();
        raise DatabaseException("Ocorreu um erro ao remover o objeto.");
    finally:
        session.close();
