from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.pessoa import Pessoa

#Definindo classe
class PessoaFisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Genero, estado_civil: EstadoCivil, data_nascimento: str,
                endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.data_nascimento = data_nascimento

#Tostring()
    def __str__(self) -> str:
        return (super().__str__() +
                f"\nSexo: {self.sexo.texto} / {self.sexo.caracter}"
                f"\nEstado Civil: {self.estado_civil.texto}"
                f"\nData de Nascimento: {self.data_nascimento}")