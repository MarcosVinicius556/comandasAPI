from fastapi import APIRouter;
from models.Funcionario import FuncionarioModel;

from services import FuncionarioService as service;

#Objeto para criação das rotas
router = APIRouter();

@router.post("/funcionario/", tags=["Funcionário"])
def create(obj: FuncionarioModel):
    newFuncionario = service.insert(obj);
    return { "id": newFuncionario.id_funcionario }, 200;

@router.get("/funcionario/", tags=["Funcionário"])
def findAll():
    funcionarios = service.findAll();
    return funcionarios, 200;

@router.get("/funcionario/{id}", tags=["Funcionário"])
def findById(id: int):
    funcionario = service.findById(id);
    return funcionario, 200;

@router.put("/funcionario/{id}", tags=["Funcionário"])
def update(id: int, obj: FuncionarioModel):
    updatedFuncionario = service.update(id, obj);
    return { "id": updatedFuncionario.id_funcionario }, 200;

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete(id: int):
    service.delete(id);
    return { "detail": "Funcionário removido com sucesso!" }, 200;

@router.get("/funcionario/cpf/{cpf}", tags=["Funcionário - Valida CPF"])
def findByCPF(cpf: str):
    funcionarios = service.findByCpf(cpf);
    return funcionarios, 200;

@router.post("/funcionario/login", tags=["Funcionário - Login"])
def findByCPFAndSenha(obj: FuncionarioModel):
    funcionario = service.findByCPFAndSenha(obj.cpf, obj.senha);
    return funcionario, 200;
