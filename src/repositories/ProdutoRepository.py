#Classe de repositório, responsável pelas operações no banco de dados

#Classe modelo de objeto para a aplicação
from models.Produto import ProdutoModel;

#Classe modelo ORM para o banco de dados
from entities.ProdutoEntity import ProdutoDB;

#Classe responsável por fornecer a conexão com o banco de dados
import config.database.DatabaseConnection as DatabaseConnection;

def insert(newProduto: ProdutoModel):
    try:
        session = DatabaseConnection.Session();
    
        obj = ProdutoDB(None, newProduto.nome, newProduto.descricao, newProduto.foto, newProduto.valor_unitario);
        
        session.begin();
        session.add(obj);
        session.commit();
        
    except Exception as e:
        session.rollback(); 
        raise e; #Criar exceções personalizadas....
    finally:
        session.close();
        
def findAll():
    try:
        session = DatabaseConnection.Session();
        
        produtos = session.query(ProdutoDB).all();
        return produtos;
    except Exception as e:
        raise e; #Criar exceções personalizadas....
    finally:
        session.close();
        
def findById(id: int):
    try:
        session = DatabaseConnection.Session();
        
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one();
        return produto;
    except Exception as e:
        raise e;
    finally:
        session.close();
        
def update(newProduto: ProdutoModel):
    try:
        session = DatabaseConnection.Session();
        
        session.begin();
        session.add(newProduto);
        session.commit();
    except Exception as e:
        session.rollback();
        raise e;
    finally:
        session.close();

def delete(produto: ProdutoModel):
    try:
        session = DatabaseConnection.Session();
        
        session.begin();
        session.delete(produto);
        session.commit();
    except Exception as e:
        session.rollback();
        raise e;
    finally:
        session.close();
