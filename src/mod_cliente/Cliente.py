from pydantic import BaseModel;

class ClienteModel(BaseModel):
    id_cliente: int = None;
    nome: str; 
    cpf: str = None;
    telefone: str = None;
    