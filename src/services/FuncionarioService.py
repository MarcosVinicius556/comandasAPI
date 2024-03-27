#Classe de serviço, responsável por regras de negócio(caso haja)

from repositories import FuncionarioRepository as repository;

from models.Funcionario import FuncionarioModel;
from entities.FuncionarioEntity import FuncionarioDB; 

def insert(newFuncionario: FuncionarioModel):
    try:
        funcionarioDB = FuncionarioDB(None, newFuncionario.nome, newFuncionario.matricula, newFuncionario.cpf, newFuncionario.telefone, newFuncionario.grupo, newFuncionario.senha);
        repository.insert(funcionarioDB)
        return newFuncionario;
    except Exception as e:
        raise e;
        
def findAll():
    try:
        funcionarios = repository.findAll();
        return funcionarios;
    except Exception as e:
        raise e;
        
def findById(id: int):
    try:
        funcionario = repository.findById(id);
        return funcionario;
    except Exception as e:
        raise e;
        
def update(id: int, newFuncionario: FuncionarioModel):
    try:
        funcionario = repository.findById(id);
        
        funcionario.nome = newFuncionario.nome;
        funcionario.matricula = newFuncionario.matricula;
        funcionario.cpf = newFuncionario.cpf;
        funcionario.telefone = newFuncionario.telefone;
        funcionario.grupo = newFuncionario.grupo;
        funcionario.senha = newFuncionario.senha;
        
        repository.update(funcionario)
        return newFuncionario;
    except Exception as e:
        raise e;

def delete(id: int):
    try:
        funcionario = findById(id);
        repository.delete(funcionario);
    except Exception as e:
        raise e;
    
def findByCpf(cpf: str):
    try:
        funcionarios = repository.findByCPF(cpf);
        return funcionarios;
    except Exception as e:
        raise e;
    
def findByCPFAndSenha(cpf: str, senha: str):
    try:
        funcionario = repository.findByCPFAndSenha(cpf, senha);
        return funcionario;
    except Exception as e:
        raise e;