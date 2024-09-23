#from abc import ABC, abstractmethod
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
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = self._verificar_salario(salario)

#Definindo exceção para atributo
    #@abstractmethod
    def _verificar_salario(self, salario):
        if salario < 0:
            raise ValueError("Salario não pode ser negativa.")
        if not isinstance(salario, double):
            raise TypeError("Digite apenas numeros.")
        return salario

#Tostring()
    def __str__(self) -> str:
        return (super().__str__(),
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nMatricula: {self.setor.texto}"
                f"\nSalario: {self.salario}"
                )