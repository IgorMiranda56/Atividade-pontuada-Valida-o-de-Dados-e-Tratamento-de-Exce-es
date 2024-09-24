import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_medico():
    medico1 = Medico(79, "Amanda", "(71)99999-7777", "amandaklein@gmail.com", Genero.FEMININO, EstadoCivil.SEPARADO, "30/01/1991", "066.611.311.77", "32971117-36",
                        "98111", Setor.SAUDE, 10000.00, "3659", Endereco("Rua K", "12", "Apartamento A", "70000-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))
    return medico1

#Validando Exceções
def test_validar_id_tipo_int(teste_medico):
    with pytest.raises(TypeError, match="Digite somente numeros inteiros para ID."):
        Medico("f", "Amanda", "(71)99999-7777", "amandaklein@gmail.com", Genero.FEMININO, EstadoCivil.SEPARADO, "30/01/1991", "066.611.311.77", "32971117-36",
                        "98111", Setor.SAUDE, 10000.00, "3659", Endereco("Rua K", "12", "Apartamento A", "70000-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_validar_id_valor_negativo(teste_medico):
    with pytest.raises(ValueError, match="Digite um numero que seja inteiro e positivo para ID."):
        Medico(-79, "Amanda", "(71)99999-7777", "amandaklein@gmail.com", Genero.FEMININO, EstadoCivil.SEPARADO, "30/01/1991", "066.611.311.77", "32971117-36",
                        "98111", Setor.SAUDE, 10000.00, "3659", Endereco("Rua K", "12", "Apartamento A", "70000-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_validar_id_nome_vazio(teste_medico):
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        Medico(79, "", "(71)99999-7777", "amandaklein@gmail.com", Genero.FEMININO, EstadoCivil.SEPARADO, "30/01/1991", "066.611.311.77", "32971117-36",
                        "98111", Setor.SAUDE, 10000.00, "3659", Endereco("Rua K", "12", "Apartamento A", "70000-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_validar_salario_tipo_valor_float(teste_medico):
    with pytest.raises(TypeError, match="Digite somente numeros reais com o ponto separando casas decimais."):
        Medico(79, "Amanda", "(71)99999-7777", "amandaklein@gmail.com", Genero.FEMININO, EstadoCivil.SEPARADO, "30/01/1991", "066.611.311.77", "32971117-36",
                        "98111", Setor.SAUDE, "g", "3659", Endereco("Rua K", "12", "Apartamento A", "70000-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_validar_salario_valor_negativo(teste_medico):
    with pytest.raises(ValueError, match="Digite um numero que seja real e positivo."):
        Medico(79, "Amanda", "(71)99999-7777", "amandaklein@gmail.com", Genero.FEMININO, EstadoCivil.SEPARADO, "30/01/1991", "066.611.311.77", "32971117-36",
                        "98111", Setor.SAUDE, -10000.00, "3659", Endereco("Rua K", "12", "Apartamento A", "70000-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))
        
#Validando Atributos
def test_validar_id_engenheiro(teste_medico):
    assert teste_medico.id == 79

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.nome == "Amanda"

def test_validar_telefone_engenheiro(teste_medico):
    assert teste_medico.telefone == "(71)99999-7777"

def test_validar_email_engenheiro(teste_medico):
    assert teste_medico.email == "amandaklein@gmail.com"

def test_validar_genero_engenheiro(teste_medico):
    assert teste_medico.sexo == Genero.FEMININO

def test_validar_estado_civil_engenheiro(teste_medico):
    assert teste_medico.estado_civil == EstadoCivil.SEPARADO

def test_validar_data_nascimento_engenheiro(teste_medico):
    assert teste_medico.data_nascimento == "30/01/1991"

def test_validar_cpf_engenheiro(teste_medico):
    assert teste_medico.cpf == "066.611.311.77"

def test_validar_rg_engenheiro(teste_medico):
    assert teste_medico.rg == "32971117-36"

def test_validar_matricula_engenheiro(teste_medico):
    assert teste_medico.matricula =="98111"

def test_validar_setor_engenheiro(teste_medico):
    assert teste_medico.setor == Setor.SAUDE

def test_validar_salario_engenheiro(teste_medico):
    assert teste_medico.salario == 10000.00

def test_validar_crea_engenheiro(teste_medico):
    assert teste_medico.crm == "3659"

def test_validar_endereco_logradouro_engenheiro(teste_medico):
    assert teste_medico.endereco.logradouro == "Rua K"

def test_validar_endereco_numero_engenheiro(teste_medico):
    assert teste_medico.endereco.numero == "12"

def test_validar_endereco_complemento_engenheiro(teste_medico):
    assert teste_medico.endereco.complemento == "Apartamento A"

def test_validar_endereco_cep_engenheiro(teste_medico):
    assert teste_medico.endereco.cep == "70000-000"

def test_validar_endereco_cidade_engenheiro(teste_medico):
    assert teste_medico.endereco.cidade == "Rio de Janeiro"

def test_validar_endereco_uf_engenheiro(teste_medico):
    assert teste_medico.endereco.uf == UnidadeFederativa.RIO_DE_JANEIRO