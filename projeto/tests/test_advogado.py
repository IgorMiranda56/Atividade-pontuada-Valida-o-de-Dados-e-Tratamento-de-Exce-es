#from abc import abstractmethod
import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def modelo_oab():
    pessoa1 = Advogado(1, "Marta", "71 9", "Mrt@gmail.com", Genero.FEMININO, EstadoCivil.CASADO,  "22/06/1995", "789", "465", "123", Setor.ENGENHARIA, 5000.0, "111", 
                       Endereco("Rua A", "345", "Avenida A", "444", "Salvador", UnidadeFederativa.BAHIA))
    return pessoa1
#@abstractmethod
def test_validando_oab(modelo_oab):
    assert modelo_oab.oab == "111"

#def test_salario_advogado(modelo_oab):
 #   with pytest.raises(ValueError, match="Digite apenas numeros."): 
  #      Advogado(1, "Marta", "71 9", "Mrt@gmail.com", Genero.FEMININO, EstadoCivil.CASADO,  "22/06/1995", "789", "465", "123", Setor.ENGENHARIA, 5000.0, "111", 
   #                    Endereco("Rua A", "345", "Avenida A", "444", "Salvador", UnidadeFederativa.BAHIA))
