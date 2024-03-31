from fastapi import APIRouter;
from models.Cliente import ClienteModel;

from services import ClienteService as service;

#Objeto para criação das rotas
router = APIRouter();

@router.post("/cliente/", tags=["Cliente"])
def create(obj: ClienteModel):
    newCliente = service.insert(obj);
    return { "id": newCliente.id_cliente }, 200;

@router.get("/cliente/", tags=["Cliente"])
def findAll():
    clientes = service.findAll();
    return clientes, 200;

@router.get("/cliente/{id}", tags=["Cliente"])
def findById(id: int):
    cliente = service.findById(id);
    return cliente, 200;

@router.put("/cliente/{id}", tags=["Cliente"])
def update(id: int, obj: ClienteModel):
    updatedCliente = service.update(id, obj);
    return { "id": updatedCliente.id_cliente }, 200;

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete(id: int):
    service.delete(id);
    return { "detail": "Cliente removido com sucesso!" }, 200;

