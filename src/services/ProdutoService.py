#Classe de serviço, responsável por regras de negócio(caso haja)

from repositories import ProdutoRepository as repository;

from models.Produto import ProdutoModel;
from entities.ProdutoEntity import ProdutoDB; 

def insert(newProduto: ProdutoModel):
    try:
        produtoDB = ProdutoDB(None, newProduto.nome, newProduto.descricao, newProduto.foto, newProduto.valor_unitario);
        repository.insert(produtoDB)
        return newProduto;
    except Exception as e:
        raise e;
        
def findAll():
    try:
        produtos = repository.findAll();
        return produtos;
    except Exception as e:
        raise e;
        
def findById(id: int):
    try:
        produto = repository.findById(id);
        return produto;
    except Exception as e:
        raise e;
        
def update(id: int, newProduto: ProdutoModel):
    try:
        produto = repository.findById(id);
        
        produto.nome = newProduto.nome;
        produto.descricao = newProduto.descricao;
        produto.foto = newProduto.foto;
        produto.valor_unitario = newProduto.valor_unitario;
        
        repository.update(produto)
        return produto;
    except Exception as e:
        raise e;

def delete(id: int):
    try:
        produto = findById(id);
        repository.delete(produto);
    except Exception as e:
        raise e;