from pydantic import BaseModel;

class FuncionarioModel(BaseModel):
    id_funcionario: int = None;
    nome: str;
    matricula: str;
    cpf: str;
    telefone: str = None;
    grupo: int;
    grupo: int;
    senha: str = None;