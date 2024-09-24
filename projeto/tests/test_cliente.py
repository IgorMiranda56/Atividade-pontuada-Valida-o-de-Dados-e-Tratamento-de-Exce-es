import pytest
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_cliente():
    cliente01 = Cliente(80, "Fernanda", "(71)99999-6666", "fernanda632@gmail.com", Genero.FEMININO, EstadoCivil.SOLTEIRO, "07/11/1985", 565698,
                        Endereco("Rua L", "9", "Apartamento 3-A", "45000-000", "Feira de Santana", UnidadeFederativa.BAHIA))
    return cliente01

#Validando Exceções
def test_validar_id_tipo_int(teste_cliente):
    with pytest.raises(TypeError, match="Digite somente numeros inteiros para ID."):
        Cliente("h", "Fernanda", "(71)99999-6666", "fernanda632@gmail.com", Genero.FEMININO, EstadoCivil.SOLTEIRO, "07/11/1985", 565698,
                        Endereco("Rua L", "9", "Apartamento 3-A", "45000-000", "Feira de Santana", UnidadeFederativa.BAHIA))

def test_validar_id_valor_negativo(teste_cliente):
    with pytest.raises(ValueError, match="Digite um numero que seja inteiro e positivo para ID."):
        Cliente(-80, "Fernanda", "(71)99999-6666", "fernanda632@gmail.com", Genero.FEMININO, EstadoCivil.SOLTEIRO, "07/11/1985", 565698,
                        Endereco("Rua L", "9", "Apartamento 3-A", "45000-000", "Feira de Santana", UnidadeFederativa.BAHIA))

def test_validar_id_nome_vazio(teste_cliente):
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        Cliente(80, "", "(71)99999-6666", "fernanda632@gmail.com", Genero.FEMININO, EstadoCivil.SOLTEIRO, "07/11/1985", 565698,
                        Endereco("Rua L", "9", "Apartamento 3-A", "45000-000", "Feira de Santana", UnidadeFederativa.BAHIA))

def test_validar_protocolo_atendimento_tipo_int(teste_cliente):
    with pytest.raises(TypeError, match="Digite somente numeros inteiros para cliente."):
        Cliente(80, "Fernanda", "(71)99999-6666", "fernanda632@gmail.com", Genero.FEMININO, EstadoCivil.SOLTEIRO, "07/11/1985", "k",
                        Endereco("Rua L", "9", "Apartamento 3-A", "45000-000", "Feira de Santana", UnidadeFederativa.BAHIA))

def test_validar_protocolo_atendimento_valor_negativo(teste_cliente):
    with pytest.raises(ValueError, match="Digite um numero que seja inteiro e positivo para cliente."):
        Cliente(80, "Fernanda", "(71)99999-6666", "fernanda632@gmail.com", Genero.FEMININO, EstadoCivil.SOLTEIRO, "07/11/1985", -565698,
                        Endereco("Rua L", "9", "Apartamento 3-A", "45000-000", "Feira de Santana", UnidadeFederativa.BAHIA))
        
#Validando Atributos
def test_validar_id_cliente(teste_cliente):
    assert teste_cliente.id == 80

def test_validar_nome_cliente(teste_cliente):
    assert teste_cliente.nome == "Fernanda"

def test_validar_telefone_cliente(teste_cliente):
    assert teste_cliente.telefone == "(71)99999-6666"

def test_validar_email_cliente(teste_cliente):
    assert teste_cliente.email == "fernanda632@gmail.com"

def test_validar_genero_cliente(teste_cliente):
    assert teste_cliente.sexo == Genero.FEMININO

def test_validar_estado_civil_cliente(teste_cliente):
    assert teste_cliente.estado_civil == EstadoCivil.SOLTEIRO

def test_validar_data_nascimento_cliente(teste_cliente):
    assert teste_cliente.data_nascimento == "07/11/1985"

def test_validar_protocolo_atendimento_cliente(teste_cliente):
    assert teste_cliente.protocolo_atendimento == 565698

def test_validar_endereco_logradouro_cliente(teste_cliente):
    assert teste_cliente.endereco.logradouro == "Rua L"

def test_validar_endereco_numero_cliente(teste_cliente):
    assert teste_cliente.endereco.numero == "9"

def test_validar_endereco_complemento_cliente(teste_cliente):
    assert teste_cliente.endereco.complemento == "Apartamento 3-A"

def test_validar_endereco_cep_cliente(teste_cliente):
    assert teste_cliente.endereco.cep == "45000-000"

def test_validar_endereco_cidade_cliente(teste_cliente):
    assert teste_cliente.endereco.cidade == "Feira de Santana"

def test_validar_endereco_uf_cliente(teste_cliente):
    assert teste_cliente.endereco.uf == UnidadeFederativa.BAHIA