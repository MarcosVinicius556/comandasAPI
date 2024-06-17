from fastapi import FastAPI;
from settings import HOST, PORT, RELOAD;

#Import das rotas
from mod_funcionario import FuncionarioDAO;
from mod_cliente import ClienteDAO;
from mod_produto import ProdutoDAO;
from mod_comanda import ComandaDAO;
from mod_report import ReportGeneratorDAO;
import security;

import db;

app = FastAPI();

#Definindo um tratamento para a "rota padrão"
@app.get("/")
def root():
    return {"detail": "API Pastelaria", "SwaggerUI": "http://127.0.0.1:8000/docs", "Redoc": "http://127.0.0.1:8000/redoc"}, 200

#Atribuindo as rotas para a aplicação
app.include_router(FuncionarioDAO.router);
app.include_router(ClienteDAO.router);
app.include_router(ProdutoDAO.router);
app.include_router(ComandaDAO.router);
app.include_router(ReportGeneratorDAO.router)
app.include_router(security.router);

#Caso não exista, cria as tabelas no banco de dados
db.criaTabelas();

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=RELOAD);