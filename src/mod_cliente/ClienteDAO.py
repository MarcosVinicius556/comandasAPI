from fastapi import APIRouter;

from mod_cliente.Cliente import ClienteModel;

#Objeto para criação das rotas
router = APIRouter();

#Definição das rotas
@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return { "msg": "GET todos executado" }, 200;

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    return { "msg": "GET um executado" }, 200;

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(f: ClienteModel):
    return { "msg": "POST executado", "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone }, 200;

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, f: ClienteModel):
    return { "msg": "PUT executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone }, 201;

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return { "msg": "DELETE executado" }, 201;


