#Encapsula informações de exceções para padronizar um retorno
from datetime import datetime;

class StandardError:
    timestamp: str;
    status: int;
    error: str;
    message: str;
    
    #"Construtor padrão"
    def __init__(self, status: int, error: str, message: str) -> None:
        self.timestamp = datetime.now().isoformat(); #Sempre pega a data em que foi criado e formata para String
        self.status = status;
        self.error = error;
        self.message = message;