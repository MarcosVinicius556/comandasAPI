#Este arquivo irá ficar responsável por importar dependência necessárias para 
#a conexão com o banco de dados
from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.ext.declarative import declarative_base;
from config.database.DatabaseConfig import STR_DATABASE;

#Cria um mecanismo de conexão com o banco de dados
engine = create_engine(STR_DATABASE, echo=True);

#Criará as sessões que iremos utilizar nas nossas transações com o banco de dados
Session = sessionmaker(bind=engine);

#Irá ficar responsável por "representar" as entidades no banco de dados de acordo com o mapeamento ORM
Base = declarative_base();

# Função para criar as tabelas com base no mapeamento caso não existam no banco de dados
def criaTabelas():
    Base.metadata.create_all(engine);