import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_avogado():
    advogado1 = Advogado(46, "Fernando", "(71)99999-8888", "fernando231@gmail.com", Genero.MASCULINO, EstadoCivil.DIVORCIADO, "06/11/1980", "071.659.321.77", "32978897-56",
                        "98981", Setor.JURIDICO, 7000.00, "963", Endereco("Rua P", "96", "Apartamento C", "60000-000", "São Paulo", UnidadeFederativa.SAO_PAULO))
    return advogado1

#Validando Exceções
def test_validar_id_tipo_int(teste_avogado):
    with pytest.raises(TypeError, match="Digite somente numeros inteiros para ID."):
        Advogado("f", "Fernando", "(71)99999-8888", "fernando231@gmail.com", Genero.MASCULINO, EstadoCivil.DIVORCIADO, "06/11/1980", "071.659.321.77", "32978897-56",
                        "98981", Setor.JURIDICO, 7000.00, "963", Endereco("Rua P", "96", "Apartamento C", "60000-000", "São Paulo", UnidadeFederativa.SAO_PAULO))
        
def test_validar_id_valor_negativo(teste_avogado):
    with pytest.raises(ValueError, match="Digite um numero que seja inteiro e positivo para ID."):
        Advogado(-46, "Fernando", "(71)99999-8888", "fernando231@gmail.com", Genero.MASCULINO, EstadoCivil.DIVORCIADO, "06/11/1980", "071.659.321.77", "32978897-56",
                        "98981", Setor.JURIDICO, 7000.00, "963", Endereco("Rua P", "96", "Apartamento C", "60000-000", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_validar_salario_tipo_valor_float(teste_avogado):
    with pytest.raises(TypeError, match="Digite somente numeros reais com o ponto separando casas decimais."):
        Advogado(46, "Fernando", "(71)99999-8888", "fernando231@gmail.com", Genero.MASCULINO, EstadoCivil.DIVORCIADO, "06/11/1980", "071.659.321.77", "32978897-56",
                        "98981", Setor.JURIDICO, "f", "963", Endereco("Rua P", "96", "Apartamento C", "60000-000", "São Paulo", UnidadeFederativa.SAO_PAULO))
        
def test_validar_salario_valor_negativo(teste_avogado):
    with pytest.raises(ValueError, match="Digite um numero que seja real e positivo."):
        Advogado(46, "Fernando", "(71)99999-8888", "fernando231@gmail.com", Genero.MASCULINO, EstadoCivil.DIVORCIADO, "06/11/1980", "071.659.321.77", "32978897-56",
                        "98981", Setor.JURIDICO, -7000.00, "963", Endereco("Rua P", "96", "Apartamento C", "60000-000", "São Paulo", UnidadeFederativa.SAO_PAULO))

#Validando Atributos
def test_validar_id_advogado(teste_avogado):
    assert teste_avogado.id == 46

def test_validar_nome_advogado(teste_avogado):
    assert teste_avogado.nome == "Fernando"

def test_validar_telefone_advogado(teste_avogado):
    assert teste_avogado.telefone == "(71)99999-8888"

def test_validar_email_advogado(teste_avogado):
    assert teste_avogado.email == "fernando231@gmail.com"

def test_validar_genero_advogado(teste_avogado):
    assert teste_avogado.sexo == Genero.MASCULINO

def test_validar_estado_civil_advogado(teste_avogado):
    assert teste_avogado.estado_civil == EstadoCivil.DIVORCIADO

def test_validar_data_nascimento_advogado(teste_avogado):
    assert teste_avogado.data_nascimento == "06/11/1980"

def test_validar_cpf_advogado(teste_avogado):
    assert teste_avogado.cpf == "071.659.321.77"

def test_validar_rg_advogado(teste_avogado):
    assert teste_avogado.rg == "32978897-56"

def test_validar_matricula_advogado(teste_avogado):
    assert teste_avogado.matricula == "98981"

def test_validar_setor_advogado(teste_avogado):
    assert teste_avogado.setor == Setor.JURIDICO

def test_validar_salario_advogado(teste_avogado):
    assert teste_avogado.salario == 7000.00

def test_validar_crea_advogado(teste_avogado):
    assert teste_avogado.oab == "963"

def test_validar_endereco_logradouro_advogado(teste_avogado):
    assert teste_avogado.endereco.logradouro == "Rua P"

def test_validar_endereco_numero_advogado(teste_avogado):
    assert teste_avogado.endereco.numero == "96"

def test_validar_endereco_complemento_advogado(teste_avogado):
    assert teste_avogado.endereco.complemento == "Apartamento C"

def test_validar_endereco_cep_advogado(teste_avogado):
    assert teste_avogado.endereco.cep == "60000-000"

def test_validar_endereco_cidade_advogado(teste_avogado):
    assert teste_avogado.endereco.cidade == "São Paulo"

def test_validar_endereco_uf_advogado(teste_avogado):
    assert teste_avogado.endereco.uf == UnidadeFederativa.SAO_PAULO