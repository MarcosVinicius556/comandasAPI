#Esta classe ficará responsável por tratar as exceções lançadas na camada de recurso da aplicação
from fastapi import Request;
from fastapi.responses import JSONResponse;

from resources.exceptions.StandardError import StandardError;

from services.exceptions.DatabaseException import DatabaseException;
from services.exceptions.ResourceNotFoundException import ResourceNotFoundException;

#Trata o tipo mais genérico de erro em requisições "Exception"
async def default_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    
    status = 500;
    error = str(exc);
    message = "Ocorreu um erro interno no servidor.";
    
    standard_error = StandardError(status=status, error=error, message=message);
    #__dict__ "retorna o objeto em JSON"
    return JSONResponse( content=standard_error.__dict__ );

#Trata exceção genéricas operações de banco 
async def database_exception_handler(request: Request, exc: DatabaseException) -> JSONResponse:
    
    status = 500;
    error = str(exc);
    message = "Ocorreu um erro ao tentar efetuar a operação no banco de dados";
    
    standard_error = StandardError(status=status, error=error, message=message);
    return JSONResponse( content=standard_error.__dict__ );

#Trata exceção genéricas operações de banco 
async def resource_not_found_exception_handler(request: Request, exc: ResourceNotFoundException) -> JSONResponse:
    
    status = 404;
    error = str(exc);
    message = "Nenhum objeto encontrado!";
    
    standard_error = StandardError(status=status, error=error, message=message);
    return JSONResponse( content=standard_error.__dict__ );
