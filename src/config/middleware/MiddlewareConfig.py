from fastapi import FastAPI

from config.auth.AuthConfig import verifica_token;

def configure_middlewares(app: FastAPI):
    #Middleware de autenticação
    app.middleware("http")(verifica_token);
    
