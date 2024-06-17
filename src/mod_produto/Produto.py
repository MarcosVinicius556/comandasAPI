from pydantic import BaseModel;
from typing import Optional
from decimal import Decimal;

class ProdutoModel(BaseModel):
    id_produto: Optional[int] = None
    nome: str;
    descricao: str;
    foto: Optional[bytes] = None
    valor_unitario: Decimal = None;