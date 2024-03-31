#Classe responsável por gerar e validar o token de acesso do funcionário
from models.Funcionario import FuncionarioModel;

import jwt;

SECRET_PASS_TOKEN = "PASTELARIA_DO_ZE";

##
#   Gera um token com o CPF e SENHA de um funcionário.... 
##
async def createToken(cpf: str, senha: str) -> str:
    # Define o payload do token
    payload = {
        "CPF": cpf,
        "SENHA": senha
    }

    # Gera o token
    token = jwt.encode(payload, SECRET_PASS_TOKEN, algorithm="HS256")

    return token;
    
##
# Valida o token de um funcionário para sabe se bate com as informaçoes do banco de dados e se ainda está válido
##
async def validaToken(token: str) -> bool:

    try:
        # Tenta decodificar o token
        payload = jwt.decode(token, SECRET_PASS_TOKEN, algorithms=["HS256"])
        
        print(payload) #remover após os testes
        
        return True;
    except jwt.ExpiredSignatureError as expired:
        raise expired;
    except jwt.InvalidTokenError as invalid:
        raise invalid;