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