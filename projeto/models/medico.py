from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor
from projeto.models.funcionario import Funcionario

#Definindo classe
class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Genero, estado_civil: EstadoCivil, data_nascimento: str, cpf: str, rg: str,
                matricula: str, setor: Setor, salario: float, crm: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estado_civil, data_nascimento, cpf, rg, matricula, setor, salario, endereco)
        self.crm = crm

#Definindo exceção para atributo
    def _verificar_id(self, id: int) -> int:
        return super()._verificar_id(id)
    
    def _verificar_salario(self, salario: float) -> float:
        return super()._verificar_salario(salario)

    def _verificar_nome(self, nome: str) -> str:
        return super()._verificar_nome(nome)
    
#Tostring()
    def __str__(self) -> str:
        return (super().__str__() + 
                f"\nCRM: {self.crm}")