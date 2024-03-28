import config.database.DatabaseConnection as DatabaseConnection;

from sqlalchemy import Column, INTEGER, VARCHAR, BLOB, DECIMAL;

class ProdutoDB(DatabaseConnection.Base):
    __tablename__ = "tb_produto";
    
    id_produto = Column(INTEGER, primary_key=True, autoincrement=True, index=True);
    nome = Column(VARCHAR(100), nullable=False);
    descricao = Column(VARCHAR(200), nullable=False);
    foto = Column(BLOB, nullable=True);
    valor_unitario = Column(DECIMAL(11,2), nullable=False);