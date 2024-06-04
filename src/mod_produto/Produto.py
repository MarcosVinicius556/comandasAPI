from pydantic import BaseModel;
from decimal import Decimal;

class ProdutoModel(BaseModel):
    id_produto: int = None;
    nome: str;
    descricao: str;
    foto: bytes = None;
    valor_unitario: Decimal = None;