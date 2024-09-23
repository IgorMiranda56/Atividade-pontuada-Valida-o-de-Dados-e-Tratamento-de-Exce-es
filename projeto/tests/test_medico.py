import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def modelo_crm():
    pessoa1 = Medico(1, "Marta", "71 9", "Mrt@gmail.com", Genero.FEMININO, EstadoCivil.CASADO,  "22/06/1995", "789", "465", "123", Setor.ENGENHARIA, 5000.0, "111", 
                       Endereco("Rua A", "345", "Avenida A", "444", "Salvador", UnidadeFederativa.BAHIA))
    return pessoa1
#@abstractmethod
def test_validando_crm(modelo_crm):
    assert modelo_crm.crm == "111"