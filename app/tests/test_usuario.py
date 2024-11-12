import pytest
from app.models.usuario_models import Usuario
from app.config.database import db
import os 

os.system("cls||clear")

import pytest
from app.models.usuario_models import Usuario

def test_usuario_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("", "arthur@gmail.com", "54321")

def test_usuario_nome_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario(000, "arthur@gmail.com", "54321") 

def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("arthur", "", "54321")

def test_usuario_email_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("arthur", 000, "54321")  

def test_usuario_senha_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("arthur", "arthur@gmail.com", "")

def test_usuario_senha_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("arthur", "arthur@gmail.com", 54321)  