from abc import abstractmethod
from numpy import double
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor
from projeto.models.funcionario import Funcionario

#Definindo classes
class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, genero: Genero, estado_civil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str,
                setor: Setor, salario: double, crea: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, genero, estado_civil, dataNascimento, cpf, rg, matricula, setor, salario, endereco)
        self.crea = crea
        
    @abstractmethod
    def _verificar_salario(self, salario) -> float:
        return 

    def _verificar_id(self, id) -> int:
        pass
#Tostring()
    def __str__(self) -> str:
        return (super().__str__(),
                f"\nCREA: {self.crea}")