#Classe de serviço, responsável por regras de negócio(caso haja)

from repositories import FuncionarioRepository as repository;

from models.Funcionario import FuncionarioModel;
from entities.FuncionarioEntity import FuncionarioDB; 

from services.exceptions.DatabaseException import DatabaseException;
from services.exceptions.ResourceNotFoundException import ResourceNotFoundException;
from config.auth.TokenUtil import createToken;

def insert(newFuncionario: FuncionarioModel):
    try:
        funcionarioDB = FuncionarioDB(None, newFuncionario.nome, newFuncionario.matricula, newFuncionario.cpf, newFuncionario.telefone, newFuncionario.grupo, newFuncionario.senha);
        repository.insert(funcionarioDB)
        return newFuncionario;
    except DatabaseException as databaseException:
        raise databaseException;
        
def findAll():
    try:
        funcionarios = repository.findAll();
        if len(funcionarios) == 0:
            raise ResourceNotFoundException("Nenhum objeto encontrado.");
        return funcionarios;
    except DatabaseException as databaseException:
        raise databaseException;
        
def findById(id: int):
    try:
        funcionario = repository.findById(id);
        if funcionario is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        return funcionario;
    except DatabaseException as databaseException:
        raise databaseException;
        
def update(id: int, newFuncionario: FuncionarioModel):
    try:
        funcionario = repository.findById(id);
        
        if funcionario is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        
        funcionario.nome = newFuncionario.nome;
        funcionario.matricula = newFuncionario.matricula;
        funcionario.cpf = newFuncionario.cpf;
        funcionario.telefone = newFuncionario.telefone;
        funcionario.grupo = newFuncionario.grupo;
        funcionario.senha = newFuncionario.senha;
        
        repository.update(funcionario)
        return newFuncionario;
    except DatabaseException as databaseException:
        raise databaseException;

def delete(id: int):
    try:
        funcionario = findById(id);
        
        if funcionario is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        
        repository.delete(funcionario);
    except DatabaseException as databaseException:
        raise databaseException;
    
def findByCpf(cpf: str):
    try:
        funcionarios = repository.findByCPF(cpf);
        
        if len(funcionarios) == 0:
            raise ResourceNotFoundException(f"nenhum funcionário encontrado com o CPF {cpf}");
        
        return funcionarios;
    except Exception as e:
        raise e;
    
def login(cpf: str, senha: str):
    try:
        funcionario = repository.findByCPFAndSenha(cpf, senha);
        if funcionario is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o CPF {cpf} e SENHA {senha}");
        return createToken(funcionario.id_funcionario);
    except DatabaseException as databaseException:
        raise databaseException;