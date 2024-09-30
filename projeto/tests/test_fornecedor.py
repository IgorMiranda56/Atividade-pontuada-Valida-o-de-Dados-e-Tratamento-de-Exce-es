import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_fornecedor():
    fornecedor1 = Fornecedor(400, "Aco Forte", "(75)99999-3333", "acoforte@gmail.com", "798889/0001", "63213339", "Rolamento de Aço",
                                          Endereco("Rua RU", "1331", "Setor D", "49000-000", "Camacari", UnidadeFederativa.BAHIA))
    return fornecedor1

#Validando Exceções
def test_validar_id_tipo_int(teste_fornecedor):
    with pytest.raises(TypeError, match="Digite somente numeros inteiros para ID."):
       Fornecedor("o", "Aco Forte", "(75)99999-3333", "acoforte@gmail.com", "798889/0001", "63213339", "Rolamento de Aço",
                                          Endereco("Rua RU", "1331", "Setor D", "49000-000", "Camacari", UnidadeFederativa.BAHIA))

def test_validar_id_valor_negativo(teste_fornecedor):
    with pytest.raises(ValueError, match="Digite um numero que seja inteiro e positivo para ID."):
        Fornecedor(-400, "Aco Forte", "(75)99999-3333", "acoforte@gmail.com", "798889/0001", "63213339", "Rolamento de Aço",
                                          Endereco("Rua RU", "1331", "Setor D", "49000-000", "Camacari", UnidadeFederativa.BAHIA))

def test_validar_id_nome_vazio(teste_fornecedor):
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        Fornecedor(400, "", "(75)99999-3333", "acoforte@gmail.com", "798889/0001", "63213339", "Rolamento de Aço",
                                          Endereco("Rua RU", "1331", "Setor D", "49000-000", "Camacari", UnidadeFederativa.BAHIA))

def test_validar_nome_tipo(teste_fornecedor):
    with pytest.raises(TypeError, match="O nome deveria ser um texto."):
        Fornecedor(400, 123, "(75)99999-3333", "acoforte@gmail.com", "798889/0001", "63213339", "Rolamento de Aço",
                                          Endereco("Rua RU", "1331", "Setor D", "49000-000", "Camacari", UnidadeFederativa.BAHIA))
        
#Validando Atributos
def test_validar_id_fornecedor(teste_fornecedor):
    assert teste_fornecedor.id == 400

def test_validar_nome_fornecedor(teste_fornecedor):
    assert teste_fornecedor.nome == "Aco Forte"

def test_validar_telefone_fornecedor(teste_fornecedor):
    assert teste_fornecedor.telefone == "(75)99999-3333"

def test_validar_email_fornecedor(teste_fornecedor):
    assert teste_fornecedor.email == "acoforte@gmail.com"

def test_validar_cnpj_fornecedor(teste_fornecedor):
    assert teste_fornecedor.cpnj == "798889/0001"

def test_validar_inscricao_estadual_fornecedor(teste_fornecedor):
    assert teste_fornecedor.inscricao_estadual == "63213339"

def test_validar_produto_fornecedor(teste_fornecedor):
    assert teste_fornecedor.produto == "Rolamento de Aço"

def test_validar_endereco_logradouro_fornecedor(teste_fornecedor):
    assert teste_fornecedor.endereco.logradouro == "Rua RU"

def test_validar_endereco_numero_fornecedor(teste_fornecedor):
    assert teste_fornecedor.endereco.numero == "1331"

def test_validar_endereco_complemento_fornecedor(teste_fornecedor):
    assert teste_fornecedor.endereco.complemento == "Setor D"

def test_validar_endereco_cep_fornecedor(teste_fornecedor):
    assert teste_fornecedor.endereco.cep == "49000-000"

def test_validar_endereco_cidade_fornecedor(teste_fornecedor):
    assert teste_fornecedor.endereco.cidade == "Camacari"

def test_validar_endereco_uf_fornecedor(teste_fornecedor):
    assert teste_fornecedor.endereco.uf == UnidadeFederativa.BAHIA