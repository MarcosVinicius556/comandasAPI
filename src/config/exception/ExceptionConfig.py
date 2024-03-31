#Configuração dos handlers de exceções disponíveis para a aplicação
from fastapi import FastAPI;
from resources.exceptions.ResourceExceptionHandler import default_exception_handler;

def config_exception_handlers(app: FastAPI):
    app.add_exception_handler(Exception, default_exception_handler);