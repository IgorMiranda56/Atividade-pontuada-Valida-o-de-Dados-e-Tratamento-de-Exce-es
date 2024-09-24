from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa

#Definindo classe
class PessoaJuridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricao_estadual: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cpnj = cnpj
        self.inscricao_estadual = inscricao_estadual

#Tostring()
    def __str__(self) -> str:
        return (super().__str__() +
                f"\nCNPJ: {self.cpnj}"
                f"\nInscrição Estadual: {self.inscricao_estadual}")