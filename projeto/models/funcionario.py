from numpy import double
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.pessoa_fisica import PessoaFisica
from projeto.models.enums.sector import Setor

#Definindo classes
class Funcionario(PessoaFisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, genero: Genero, estado_civil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, 
                 matricula: str, setor: Setor, salario: double, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, genero, estado_civil, dataNascimento, endereco)