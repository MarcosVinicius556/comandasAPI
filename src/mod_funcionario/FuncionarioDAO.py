from fastapi import APIRouter;
from mod_funcionario.Funcionario import FuncionarioModel;

#Objeto para criação das rotas
router = APIRouter();

#Definição das rotas
@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    return { "msg": "GET todos executado" }, 200;

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return { "msg": "GET um executado" }, 200;

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(f: FuncionarioModel):
    return { "msg": "POST executado", "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone }, 200;

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, f: FuncionarioModel):
    return { "msg": "PUT executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone }, 201;

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return { "msg": "DELETE executado" }, 201;


