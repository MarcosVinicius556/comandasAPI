#Esta classe ficará responsável por tratar as exceções lançadas na camada de recurso da aplicação
from fastapi import Request;
from fastapi.responses import JSONResponse;

from resources.exceptions.StandardError import StandardError;

#Trata o tipo mais genérico de erro em requisições "Exception"
async def default_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    
    status = 500;
    error = str(exc);
    message = "Ocorreu um erro interno no servidor.";
    
    standard_error = StandardError(status=status, error=error, message=message);
    #__dict__ "retorna o objeto em JSON"
    return JSONResponse( content=standard_error.__dict__ );

