import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_engenheiro():
    engenheiro1 = Engenheiro(23, "Jose", "(71)99999-8888", "jose231@gmail.com", Genero.MASCULINO, EstadoCivil.CASADO, "23/05/1976", "077.659.321.77", "32978897-36",
                        "98989", Setor.OPERACOES, 5000.00, "321", Endereco("Rua O", "45", "Apartamento B", "40000-000", "Salvador", UnidadeFederativa.BAHIA))
    return engenheiro1

#Validando Exceções
def test_validar_id_tipo_int(teste_engenheiro):
    with pytest.raises(TypeError, match="Digite somente numeros inteiros para ID."):
        Engenheiro("ff", "Jose", "(71)99999-8888", "jose231@gmail.com", Genero.MASCULINO, EstadoCivil.CASADO, "23/05/1976", "077.659.321.77", "32978897-36",
                        "98989", Setor.OPERACOES, 5000.00, "321", Endereco("Rua O", "45", "Apartamento B", "40000-000", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_id_valor_negativo(teste_engenheiro):
    with pytest.raises(ValueError, match="Digite um numero que seja inteiro e positivo para ID."):
        Engenheiro(-23, "Jose", "(71)99999-8888", "jose231@gmail.com", Genero.MASCULINO, EstadoCivil.CASADO, "23/05/1976", "077.659.321.77", "32978897-36",
                        "98989", Setor.OPERACOES, 5000.00, "321", Endereco("Rua O", "45", "Apartamento B", "40000-000", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_salario_tipo_valor_float(teste_engenheiro):
    with pytest.raises(TypeError, match="Digite somente numeros reais com o ponto separando casas decimais."):
        Engenheiro(23, "Jose", "(71)99999-8888", "jose231@gmail.com", Genero.MASCULINO, EstadoCivil.CASADO, "23/05/1976", "077.659.321.77", "32978897-36",
                        "98989", Setor.OPERACOES, "f", "321", Endereco("Rua O", "45", "Apartamento B", "40000-000", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_salario_valor_negativo(teste_engenheiro):
    with pytest.raises(ValueError, match="Digite um numero que seja real e positivo."):
        Engenheiro(23, "Jose", "(71)99999-8888", "jose231@gmail.com", Genero.MASCULINO, EstadoCivil.CASADO, "23/05/1976", "077.659.321.77", "32978897-36",
                        "98989", Setor.OPERACOES, -5000.00, "321", Endereco("Rua O", "45", "Apartamento B", "40000-000", "Salvador", UnidadeFederativa.BAHIA))
      
#Validando Atributos
def test_validar_id_engenheiro(teste_engenheiro):
    assert teste_engenheiro.id == 23

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.nome == "Jose"

def test_validar_telefone_engenheiro(teste_engenheiro):
    assert teste_engenheiro.telefone == "(71)99999-8888"

def test_validar_email_engenheiro(teste_engenheiro):
    assert teste_engenheiro.email == "jose231@gmail.com"

def test_validar_genero_engenheiro(teste_engenheiro):
    assert teste_engenheiro.sexo == Genero.MASCULINO

def test_validar_estado_civil_engenheiro(teste_engenheiro):
    assert teste_engenheiro.estado_civil == EstadoCivil.CASADO

def test_validar_data_nascimento_engenheiro(teste_engenheiro):
    assert teste_engenheiro.data_nascimento == "23/05/1976"

def test_validar_cpf_engenheiro(teste_engenheiro):
    assert teste_engenheiro.cpf == "077.659.321.77"

def test_validar_rg_engenheiro(teste_engenheiro):
    assert teste_engenheiro.rg == "32978897-36"

def test_validar_matricula_engenheiro(teste_engenheiro):
    assert teste_engenheiro.matricula == "98989"

def test_validar_setor_engenheiro(teste_engenheiro):
    assert teste_engenheiro.setor == Setor.OPERACOES

def test_validar_salario_engenheiro(teste_engenheiro):
    assert teste_engenheiro.salario == 5000.00

def test_validar_crea_engenheiro(teste_engenheiro):
    assert teste_engenheiro.crea == "321"

def test_validar_endereco_logradouro_engenheiro(teste_engenheiro):
    assert teste_engenheiro.endereco.logradouro == "Rua O"

def test_validar_endereco_numero_engenheiro(teste_engenheiro):
    assert teste_engenheiro.endereco.numero == "45"

def test_validar_endereco_complemento_engenheiro(teste_engenheiro):
    assert teste_engenheiro.endereco.complemento == "Apartamento B"

def test_validar_endereco_cep_engenheiro(teste_engenheiro):
    assert teste_engenheiro.endereco.cep == "40000-000"

def test_validar_endereco_cidade_engenheiro(teste_engenheiro):
    assert teste_engenheiro.endereco.cidade == "Salvador"

def test_validar_endereco_uf_engenheiro(teste_engenheiro):
    assert teste_engenheiro.endereco.uf == UnidadeFederativa.BAHIA