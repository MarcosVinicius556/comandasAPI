#Serviço de autenticação da aplicação
#Responsável por verificar se um token é válido
from fastapi import Request;
from fastapi.responses import JSONResponse;
from typing import Optional;
from resources.exceptions.StandardError import StandardError;
from config.auth.TokenUtil import validaToken;

#Rotas que dispensam autenticação
DOCS_ROUTE = "/docs";
REDOC_ROUTE = "/redoc";
OPEN_API_JSON = "/openapi.json";
LOGIN_ROUTE = "/funcionario/login";

async def verifica_token(request: Request, call_next) -> JSONResponse :
    # #capturando o cabeçalho da requisição
    auth_credential: Optional[str] = request.headers.get("Authorization");
    
    isFreeRoutes = request.url.path in [DOCS_ROUTE, REDOC_ROUTE, LOGIN_ROUTE, OPEN_API_JSON] ;
    #Se não for login, verifica o token
    if not isFreeRoutes:
        #Se o token não estiver informado, não deixa prosseguir para a validação de token
        if not auth_credential or not auth_credential.startswith("Bearer"):
            status = 403;
            error = str("Acesso negado!");
            message = "Esta rota precisa de um token válido para poder ser acessada!";

            standard_error = StandardError(status=status, error=error, message=message);
            return JSONResponse( content=standard_error.__dict__ );
        
    
        #Valida o token informado
        token = auth_credential.split(" ")[1];
        tokenValido = validaToken(token);
        if tokenValido == False:
            status = 403;
            error = str("Acesso negado!");
            message = "Este token não é válido!";

            standard_error = StandardError(status=status, error=error, message=message);
            return JSONResponse( content=standard_error.__dict__ );

    return await call_next(request);