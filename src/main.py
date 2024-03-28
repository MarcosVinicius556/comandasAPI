from fastapi import FastAPI;
from config.database.DatabaseConfig import HOST, PORT, RELOAD;

#Import das rotas
from resources import FuncionarioResource;
from resources import ClienteResource;
from resources import ProdutoResource;

import config.database.DatabaseConnection as DatabaseConnection;

app = FastAPI();

#Definindo um tratamento para a "rota padrão"
@app.get("/")
def root():
    return {"detail": "API Pastelaria", "SwaggerUI": "http://127.0.0.1:8000/docs", "Redoc": "http://127.0.0.1:8000/redoc"}, 200

#Atribuindo as rotas para a aplicação
app.include_router(FuncionarioResource.router);
app.include_router(ClienteResource.router);
app.include_router(ProdutoResource.router);

#Caso não exista, cria as tabelas no banco de dados
DatabaseConnection.criaTabelas();

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=RELOAD);