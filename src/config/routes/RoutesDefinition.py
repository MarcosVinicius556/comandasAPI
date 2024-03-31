#Configuração de todas as rotas disponíveis para a aplicação
from fastapi import FastAPI;

#Import das rotas
from resources import FuncionarioResource;
from resources import ClienteResource;
from resources import ProdutoResource;

#Atribuindo as rotas para a aplicação
def config_application_routes(app: FastAPI):
    app.include_router(FuncionarioResource.router);
    app.include_router(ClienteResource.router);
    app.include_router(ProdutoResource.router);    
    