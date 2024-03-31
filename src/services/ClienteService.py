#Classe de serviço, responsável por regras de negócio(caso haja)

from repositories import ClienteRepository as repository;

from models.Cliente import ClienteModel;
from entities.ClienteEntity import ClienteDB; 

from services.exceptions.DatabaseException import DatabaseException;
from services.exceptions.ResourceNotFoundException import ResourceNotFoundException;

def insert(newCliente: ClienteModel):
    try:
        clienteDB = ClienteDB(None, newCliente.nome, newCliente.cpf, newCliente.telefone);
        repository.insert(clienteDB)
        return newCliente;
    except DatabaseException as databaseException:
        raise databaseException;
        
def findAll():
    try:
        clientes = repository.findAll();
        
        if len(clientes) == 0:
            raise ResourceNotFoundException("Nenhum objeto encontrado.");
        
        return clientes;
    except DatabaseException as databaseException:
        raise databaseException;
        
def findById(id: int):
    try:
        cliente = repository.findById(id);
        
        if cliente is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        
        return cliente;
    except DatabaseException as databaseException:
        raise databaseException;
        
def update(id: int, newCliente: ClienteModel):
    try:
        cliente = repository.findById(id);
        
        if cliente is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        
        cliente.nome = newCliente.nome;
        cliente.cpf = newCliente.cpf;
        cliente.telefone = newCliente.telefone;
        
        repository.update(cliente)
        return newCliente;
    except DatabaseException as databaseException:
        raise databaseException;

def delete(id: int):
    try:
        cliente = findById(id);
        
        if cliente is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        
        repository.delete(cliente);
    except DatabaseException as databaseException:
        raise databaseException;