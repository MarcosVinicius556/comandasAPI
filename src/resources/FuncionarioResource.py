from fastapi import APIRouter;
from models.Funcionario import FuncionarioModel;

from services import FuncionarioService as service;

#Objeto para criação das rotas
router = APIRouter();

@router.post("/funcionario/", tags=["Funcionário"])
def create(obj: FuncionarioModel):
    try:
        newFuncionario = service.insert(obj);
        
        return { "id": newFuncionario.id_funcionario }, 200;
    except Exception as e:
        return {"erro": str(e)}, 400; #Criar um exceptionHandler

@router.get("/funcionario/", tags=["Funcionário"])
def findAll():
    try:
        funcionarios = service.findAll();
        return funcionarios, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;  #Criar um exceptionHandler

@router.get("/funcionario/{id}", tags=["Funcionário"])
def findById(id: int):
    try: 
        funcionario = service.findById(id);
        
        return funcionario, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;

@router.put("/funcionario/{id}", tags=["Funcionário"])
def update(id: int, obj: FuncionarioModel):
    try:
        updatedFuncionario = service.update(id, obj);
        
        return { "id": updatedFuncionario.id_funcionario }, 200;
    except Exception as e:
        return { "erro": str(e) }, 400;

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        service.delete(id);
    except Exception as e:
        return {"erro": str(e)}, 400

@router.get("/funcionario/cpf/{cpf}", tags=["Funcionário - Valida CPF"])
def findByCPF(cpf: str):
    try:
        funcionarios = service.findByCpf(cpf);
        
        return funcionarios, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;

@router.post("/funcionario/login", tags=["Funcionário - Login"])
def findByCPFAndSenha(obj: FuncionarioModel):
    try:
        funcionario = service.findByCPFAndSenha(obj.cpf, obj.senha);
        
        return funcionario, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;
