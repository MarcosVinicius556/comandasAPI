#Configuração dos handlers de exceções disponíveis para a aplicação
from fastapi import FastAPI;
from resources.exceptions.ResourceExceptionHandler import default_exception_handler, database_exception_handler, resource_not_found_exception_handler;

#Exceções personalizadas
from services.exceptions.DatabaseException import DatabaseException;
from services.exceptions.ResourceNotFoundException import ResourceNotFoundException;

def config_exception_handlers(app: FastAPI):
    app.add_exception_handler(Exception, default_exception_handler);
    app.add_exception_handler(DatabaseException, database_exception_handler);
    app.add_exception_handler(ResourceNotFoundException, resource_not_found_exception_handler);