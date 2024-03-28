#Classe de serviço, responsável por regras de negócio(caso haja)

from repositories import ClienteRepository as repository;

from models.Cliente import ClienteModel;
from entities.ClienteEntity import ClienteDB; 

def insert(newCliente: ClienteModel):
    try:
        clienteDB = ClienteDB(None, newCliente.nome, newCliente.cpf, newCliente.telefone);
        repository.insert(clienteDB)
        return newCliente;
    except Exception as e:
        raise e;
        
def findAll():
    try:
        clientes = repository.findAll();
        return clientes;
    except Exception as e:
        raise e;
        
def findById(id: int):
    try:
        cliente = repository.findById(id);
        return cliente;
    except Exception as e:
        raise e;
        
def update(id: int, newCliente: ClienteModel):
    try:
        cliente = repository.findById(id);
        
        cliente.nome = newCliente.nome;
        cliente.cpf = newCliente.cpf;
        cliente.telefone = newCliente.telefone;
        
        repository.update(cliente)
        return newCliente;
    except Exception as e:
        raise e;

def delete(id: int):
    try:
        cliente = findById(id);
        repository.delete(cliente);
    except Exception as e:
        raise e;