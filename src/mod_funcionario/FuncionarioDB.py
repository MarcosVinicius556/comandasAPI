import db;
from sqlalchemy import Column, VARCHAR, CHAR, Integer;

#Mapeamento ORM
class FuncionarioDB(db.Base):
    #Atributo obrigatório, ele que ficará responsável por definir o nome da tabela no banco
    #Semelhante ao @Table( name = "tb_funcionario" ) utilizado em JPA
    __tablename__ = 'tb_funcionario';
    
    #Definindo as colunas, e o tipo de cada uma
    id_funcionario = Column(Integer, primary_key=True, autoincrement=True, index=True);
    nome = Column(VARCHAR(100), nullable=False);
    matricula = Column(CHAR(10), nullable=False);
    cpf = Column(CHAR(11), unique=True, nullable=False);
    telefone = Column(CHAR(11), nullable=False);
    grupo = Column(Integer, nullable=False);
    senha = Column(VARCHAR(200), nullable=False);
    
    #Definindo um construtor
    def __init__(self, id_funcionario, nome, matricula, cpf, telefone, grupo, senha):
        self.id_funcionario = id_funcionario;
        self.nome = nome;
        self.matricula = matricula;
        self.cpf = cpf;
        self.telefone = telefone;
        self.grupo = grupo;
        self.senha = senha;