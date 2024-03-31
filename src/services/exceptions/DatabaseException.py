#Exceção personalizada para error mais genéricos de banco de dados
class DatabaseException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg); #Extendemos da classe principal de exceção