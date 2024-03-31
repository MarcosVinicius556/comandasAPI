from fastapi import FastAPI;
from config.database.DatabaseConfig import HOST, PORT, RELOAD;

#Configurações gerais da aplicação
from config.routes.RoutesDefinition import config_application_routes;
from config.exception.ExceptionConfig import config_exception_handlers;

import config.database.DatabaseConnection as DatabaseConnection;

app = FastAPI();

#Definindo um tratamento para a "rota padrão"
@app.get("/")
def root():
    return {"detail": "API Pastelaria", "SwaggerUI": "http://127.0.0.1:8000/docs", "Redoc": "http://127.0.0.1:8000/redoc"}, 200

#Configuração das rotas da aplicação
config_application_routes(app);

#Configuração dos ExceptionHandlers da aplicação
config_exception_handlers(app)

#Caso não exista, cria as tabelas no banco de dados
DatabaseConnection.criaTabelas();


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=RELOAD);