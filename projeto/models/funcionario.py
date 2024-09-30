from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.sector import Setor 
from projeto.models.pessoa_fisica import PessoaFisica

#Definindo classe
class Funcionario(PessoaFisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Genero, estado_civil: EstadoCivil, data_nascimento: str,
                cpf: str, rg: str,idade: int, matricula: str, setor: Setor, salario: float, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estado_civil, data_nascimento, endereco)
        self.cpf = cpf
        self.rg = rg
        self.idade = self._verificar_idade(idade)
        self.matricula = matricula
        self.setor = setor
        self.salario = self._verificar_salario(salario)
    
#Definindo exceção para atributo
    def _verificar_salario(self, salario:float) -> float:
        #Método para verificar com duas exceções de salario se ele é float e se o numero é positivo.
        if not isinstance(salario, float):
            raise TypeError("Digite somente numeros reais com o ponto separando casas decimais.")
        if salario < 0:
            raise ValueError("Digite um numero que seja real e positivo.")
        return salario
    
    def _verificar_idade(self, idade:int) -> int:
        if not isinstance(idade, int):
            raise TypeError("Digite apenas números inteiros para idade.")
        if idade > 130:
            raise ValueError("A idade não pode ser acima de 130 anos.")
        if idade < 0:
            raise ValueError("A idade não pode ser menor que zero.")
        return idade

#Tostring()
    def __str__(self) -> str:
        return (super().__str__() + 
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nIdade: {self.idade}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor.texto}"
                f"\nSalario: {self.salario}")