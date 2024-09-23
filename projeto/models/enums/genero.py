from enum import Enum

#Determinando atributos
class Genero(Enum):
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")

    def __init__(self, texto: str, caracter: str) -> None:
        self.texto = texto
        self.caracter = caracter