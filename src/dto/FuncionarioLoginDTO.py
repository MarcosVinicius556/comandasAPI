from pydantic import BaseModel

class FuncionarioLoginDTO(BaseModel):
    cpf: str
    senha: str