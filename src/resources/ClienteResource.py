from fastapi import APIRouter;
from models.Cliente import ClienteModel;

from services import ClienteService as service;

#Objeto para criação das rotas
router = APIRouter();

@router.post("/cliente/", tags=["Cliente"])
def create(obj: ClienteModel):
    try:
        newCliente = service.insert(obj);
        
        return { "id": newCliente.id_cliente }, 200;
    except Exception as e:
        return {"erro": str(e)}, 400; #Criar um exceptionHandler

@router.get("/cliente/", tags=["Cliente"])
def findAll():
    try:
        clientes = service.findAll();
        return clientes, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;  #Criar um exceptionHandler

@router.get("/cliente/{id}", tags=["Cliente"])
def findById(id: int):
    try: 
        cliente = service.findById(id);
        
        return cliente, 200;
    except Exception as e:
        return {"erro": str(e)}, 400;

@router.put("/cliente/{id}", tags=["Cliente"])
def update(id: int, obj: ClienteModel):
    try:
        updatedCliente = service.update(id, obj);
        
        return { "id": updatedCliente.id_cliente }, 200;
    except Exception as e:
        return { "erro": str(e) }, 400;

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete(id: int):
    try:
        service.delete(id);
    except Exception as e:
        return {"erro": str(e)}, 400

