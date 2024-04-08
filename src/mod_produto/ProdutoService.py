#Classe de serviço, responsável por regras de negócio(caso haja)

from repositories import ProdutoRepository as repository;

from models.Produto import ProdutoModel;
from entities.ProdutoEntity import ProdutoDB; 

from services.exceptions.DatabaseException import DatabaseException;
from services.exceptions.ResourceNotFoundException import ResourceNotFoundException;

def insert(newProduto: ProdutoModel):
    try:
        produtoDB = ProdutoDB(None, newProduto.nome, newProduto.descricao, newProduto.foto, newProduto.valor_unitario);
        repository.insert(produtoDB)
        return newProduto;
    except DatabaseException as databaseException:
        raise databaseException;
        
def findAll():
    try:
        produtos = repository.findAll();
        if len(produtos) == 0:
            raise ResourceNotFoundException("Nenhum objeto encontrado.");
        return produtos;
    except DatabaseException as databaseException:
        raise databaseException;
        
def findById(id: int):
    try:
        produto = repository.findById(id);
        if produto is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        return produto;
    except DatabaseException as databaseException:
        raise databaseException;
        
def update(id: int, newProduto: ProdutoModel):
    try:
        produto = repository.findById(id);
        
        if produto is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        
        produto.nome = newProduto.nome;
        produto.descricao = newProduto.descricao;
        produto.foto = newProduto.foto;
        produto.valor_unitario = newProduto.valor_unitario;
        
        repository.update(produto)
        return produto;
    except DatabaseException as databaseException:
        raise databaseException;

def delete(id: int):
    try:
        produto = findById(id);
        
        if produto is None:
            raise ResourceNotFoundException(f"Objeto não encontrado com o ID. {id}");
        
        repository.delete(produto);
    except DatabaseException as databaseException:
        raise databaseException;