from fastapi import APIRouter;
from fastapi.responses import StreamingResponse;
from fastapi import Depends;
from security import get_current_active_user;
from reportlab.lib.pagesizes import letter;
from reportlab.pdfgen import canvas;
import db;
import io;

from mod_cliente.ClienteDB import ClienteDB;
from mod_funcionario.FuncionarioDB import FuncionarioDB;
from mod_produto.ProdutoDB import ProdutoDB;



#Objeto para criação das rotas
router = APIRouter(dependencies=[Depends(get_current_active_user)]);

@router.get("/export/pdf/{type}", tags=["Relatórios"])
def generate_report(type: int):
    buffer = io.BytesIO()
    
    c = canvas.Canvas(buffer, pagesize=letter)
    
    if type == 1:
        c = exportDataFuncionarios(c);
    elif type == 2:
        c = exportDataClientes(c);
    elif type == 3:
        c = exportDataProdutos(c);
        
    
    c.showPage()
    c.save()
    
    buffer.seek(0)
    
    headers = {
        'Content-Disposition': 'attachment; filename="relatorio.pdf"'
    }
    return StreamingResponse(buffer, headers=headers, media_type='application/pdf')

def exportDataFuncionarios(c: canvas.Canvas):
    c.drawString(100, 750, "Relatório de Exemplo")
    data = findAllFuncionarios();
    print("CONTEÚDO DA LISTA")
    print(data)
    y = 700
    for item in data:
        text = f"Nome: {item.nome}, Matricula: {item.matricula}, CPF: {item.cpf}, Telefone: {item.telefone}, Grupo: {item.grupo}"
        c.drawString(100, y, text)
        y -= 20

    return c;

def findAllFuncionarios():
    try:
        session = db.Session();
        
        funcionarios = session.query(FuncionarioDB).all();
        return funcionarios;
    except Exception as e:
        return {"erro": str(e)}
    finally:
        session.close();

def exportDataClientes(c: canvas.Canvas):
    c.drawString(100, 750, "Relatório de Exemplo")
    data = findAllClientes();
    
    y = 700
    for item in data:
        text = f"Nome: {item.nome}, CPF: {item.cpf}, Telefone: {item.telefone}"
        c.drawString(100, y, text)
        y -= 20

    return c;

def findAllClientes():
    try:
        session = db.Session();
        
        clientes = session.query(ClienteDB).all();
        return clientes
    except Exception as e:
        return {"erro": str(e)}
    finally:
        session.close();

def exportDataProdutos(c: canvas.Canvas):
    c.drawString(100, 750, "Relatório de Exemplo")
    data = findAllProdutos();
    
    y = 700
    for item in data:
        text = f"Nome: {item.nome}, Descrição: {item.descricao}, Valor: {item.valor_unitario}"
        c.drawString(100, y, text)
        y -= 20

    return c;

def findAllProdutos():
    try:
        session = db.Session();
        
        produtos = session.query(ProdutoDB).all();
        return produtos
    except Exception as e:
        return {"erro": str(e)}
    finally:
        session.close();