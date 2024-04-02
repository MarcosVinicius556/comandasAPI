from datetime import datetime, timedelta

#Classe responsável por gerar e validar o token de acesso do funcionário
from models.Funcionario import FuncionarioModel;

#Serviços do funcionário
from services import FuncionarioService as funcionario_service;

import jwt;

SECRET_PASS_TOKEN = "PASTELARIA_DO_ZE";

##
#   Gera um token com o CPF e SENHA de um funcionário.... 
##
def createToken(id_funcionario: int) -> str:
    # O token irá expirar em 10 minutos
    expira_em = datetime.now() + timedelta(minutes=10)
    
    
    # Define o payload do token
    payload = {
        "id_funcionario": id_funcionario,
        "expira_em": expira_em.isoformat()
    }
    
    # Gera o token
    token = jwt.encode(payload, SECRET_PASS_TOKEN, algorithm="HS256")

    return { "token": token, "expira_em": expira_em };
    
##
# Valida o token de um funcionário para sabe se bate com as informaçoes do banco de dados e se ainda está válido
##
def validaToken(token: str) -> bool:

    try:
        print("Começando processo de validação do token ->")
        # Tenta decodificar o token
        payload = jwt.decode(token, SECRET_PASS_TOKEN, algorithms=["HS256"])
        
        #Aqui temos acesso ao id do funcionário e o "prazo de validade" do token
        id_funcionario = payload['id_funcionario'];
        #Caso o funcionário não exista mais, lançara exceção e não permitirá mais acessar a API
        funcionario_service.findById(id_funcionario);
        
        expira_em = datetime.fromisoformat(payload['expira_em']);
        
        # Verificando se o token expirou
        if datetime.now() > expira_em :
            print("Token expirou!")
            return False;
        
        return True;
    except Exception as invalid:
        # raise invalid;
        print(f"Token inválido! {str(invalid)}")
        return False;