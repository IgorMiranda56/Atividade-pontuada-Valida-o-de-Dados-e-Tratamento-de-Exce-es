import pytest
from projeto.models.prestacao_servico import PrestacaoServico 
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_prestacao_servico():
    prestacao_servico1 = PrestacaoServico(103, "KAIPE SOLUCOES", "(75)99999-4444", "kaypesolucoes@gmail.com", "654648/0001", "63549879", "03/01/2020", "20/02/2024",
                                          Endereco("Rua TU", "1300", "Setor F", "47000-000", "Camacari", UnidadeFederativa.BAHIA))
    return prestacao_servico1

#Validando Exceções
def test_validar_id_tipo_int(teste_prestacao_servico):
    with pytest.raises(TypeError, match="Digite somente numeros inteiros para ID."):
       PrestacaoServico("t", "KAIPE SOLUCOES", "(75)99999-4444", "kaypesolucoes@gmail.com", "654648/0001", "63549879", "03/01/2020", "20/02/2024",
                                          Endereco("Rua TU", "1300", "Setor F", "47000-000", "Camacari", UnidadeFederativa.BAHIA)) 

def test_validar_id_valor_negativo(teste_prestacao_servico):
    with pytest.raises(ValueError, match="Digite um numero que seja inteiro e positivo para ID."):
        PrestacaoServico(-103, "KAIPE SOLUCOES", "(75)99999-4444", "kaypesolucoes@gmail.com", "654648/0001", "63549879", "03/01/2020", "20/02/2024",
                                          Endereco("Rua TU", "1300", "Setor F", "47000-000", "Camacari", UnidadeFederativa.BAHIA))

def test_validar_id_nome_vazio(teste_prestacao_servico):
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        PrestacaoServico(103, "", "(75)99999-4444", "kaypesolucoes@gmail.com", "654648/0001", "63549879", "03/01/2020", "20/02/2024",
                                          Endereco("Rua TU", "1300", "Setor F", "47000-000", "Camacari", UnidadeFederativa.BAHIA))

def test_validar_nome_tipo(teste_prestacao_servico):
    with pytest.raises(TypeError, match="O nome deveria ser um texto."):
        PrestacaoServico(103, 123, "(75)99999-4444", "kaypesolucoes@gmail.com", "654648/0001", "63549879", "03/01/2020", "20/02/2024",
                                          Endereco("Rua TU", "1300", "Setor F", "47000-000", "Camacari", UnidadeFederativa.BAHIA))
#Validando Atributos
def test_validar_id_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.id == 103

def test_validar_nome_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.nome == "KAIPE SOLUCOES"

def test_validar_telefone_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.telefone == "(75)99999-4444"

def test_validar_email_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.email == "kaypesolucoes@gmail.com"

def test_validar_cnpj_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.cpnj == "654648/0001"

def test_validar_inscricao_estadual_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.inscricao_estadual == "63549879"

def test_validar_contrato_inicio_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.contrato_inicio == "03/01/2020"

def test_validar_contrato_fim_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.contrato_fim == "20/02/2024"

def test_validar_endereco_logradouro_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.endereco.logradouro == "Rua TU"

def test_validar_endereco_numero_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.endereco.numero == "1300"

def test_validar_endereco_complemento_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.endereco.complemento == "Setor F"

def test_validar_endereco_cep_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.endereco.cep == "47000-000"

def test_validar_endereco_cidade_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.endereco.cidade == "Camacari"

def test_validar_endereco_uf_cliente(teste_prestacao_servico):
    assert teste_prestacao_servico.endereco.uf == UnidadeFederativa.BAHIA