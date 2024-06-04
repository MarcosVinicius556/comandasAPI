import db;
from sqlalchemy import Column, CHAR, VARCHAR, INTEGER;

class ClienteDB(db.Base):
    __tablename__ = "tb_cliente";
    
    id_cliente = Column(INTEGER, primary_key=True, autoincrement=True, index=True);
    nome = Column(VARCHAR(100), nullable=False);
    cpf = Column(CHAR(11), nullable=False);
    telefone = Column(CHAR(11), nullable=False);
    