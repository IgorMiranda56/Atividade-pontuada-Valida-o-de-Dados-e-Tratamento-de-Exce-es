from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

#Definindo classe
class Pessoa(ABC):
    def __init__(self, id: int, nome:str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self.nome
        self.telefone = self.telefone
        self.email = email
        self.endereco = endereco

#Definindo exceção para atributo
    @abstractmethod
    def _verificar_id(self, id):
        if not isinstance(id, int):
            raise TypeError("Digite somento numeros.")
        return id
    
#Tostring()
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}")