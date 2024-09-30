from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

#Definindo classe
class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

#Definindo exceção para atributo
    def _verificar_id(self, id: int) -> int:
        #Método para verificar com duas exceções de ID se ele é int e se o numero é positivo.
        if not isinstance(id, int):
            raise TypeError("Digite somente numeros inteiros para ID.")
        if id < 0:
            raise ValueError("Digite um numero que seja inteiro e positivo para ID.")
        return id
    
    def _verificar_nome(self, nome: str) -> str:
        if not isinstance(nome, str):
            raise TypeError("O nome deveria ser um texto.")
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        return nome
    

#Tostring()
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}")