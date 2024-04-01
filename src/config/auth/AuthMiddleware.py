from services.exceptions.UnauthorizedException import UnauthorizedException;
from fastapi import FastAPI, Request;
from typing import Optional;

async def configure_auth_middleware(app: FastAPI):
    app.middleware("http")(verifica_token);
    
async def verifica_token(request: Request, call_next):
    #capturando o cabeçalho da requisição
    auth_credential: Optional[str] = request.headers.get("Authorization");
    
    if request.url.path != "/login" and (not auth_credential or not auth_credential.startswith("Bearer")):
        raise UnauthorizedException("Acesso negado!");
    
    response = await call_next(request);
    
    print('Passou por aqui')
    
    return response;