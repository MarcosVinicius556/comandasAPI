from dotenv import load_dotenv, find_dotenv;
import os;

#Localiza o arquivo de .env
dotenv_file = find_dotenv();

#Carrega o arquivo dotenv
load_dotenv(dotenv_file);

#Configurações do APP
HOST = os.getenv("HOST");
PORT = os.getenv("PORT");
RELOAD = os.getenv("RELOAD");

#Configurações de banco de dados
DB_SGDB = os.getenv("DB_SGDB");
DB_NAME = os.getenv("DB_NAME");

#Caso seja diferente de SqLite será necessário estas variáveis
DB_HOST = os.getenv("DB_HOST");
DB_USER = os.getenv("DB_USER");
DB_PASS = os.getenv("DB_PASS");

# Ajusta a string de conexão com o banco de acordo com o que foi configurado na no arquivo .env
if DB_SGDB == 'sqlite':
    STR_DATABASE = f"sqlite:///{DB_NAME}.db"
elif DB_SGDB == 'mysql':
    STR_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
elif DB_SGDB == 'mssql':
    STR_DATABASE = f"mssql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8"
else:
    STR_DATABASE = f"sqlite:///apiDatabase.db"
    
# Configurações Segurança da API
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))