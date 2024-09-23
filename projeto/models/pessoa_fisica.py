from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estado_civil import EstadoCivil

#Definindo classe
class PessoaFisica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, genero: Genero, estado_civil: EstadoCivil, dataNascimento: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.genero = genero
        self.estado_civil = estado_civil
        self.dataNascimento = dataNascimento
    
#Tostring()
    def __str__(self) -> str:
        return (super().__str__(),
                f"\nGenero: {self.genero.texto}", " / ", {self.genero.caracter},
                f"\nEstado Civil: {self.estado_civil.texto}"
                f"\nData de Nascimento: {self.dataNascimento}")