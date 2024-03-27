#Classe responsável pela verificação o token de um usuário é válida
from fastapi import FastAPI, Depends, HTTPException, status;
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials;
import jwt;
from datetime import datetime, timedelta;