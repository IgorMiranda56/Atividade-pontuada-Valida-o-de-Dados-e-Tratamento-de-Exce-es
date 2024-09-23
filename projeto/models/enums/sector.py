from enum import Enum

#Determinando atributos
class Setor(Enum):
    ENGENHARIA = ("Engenharia")
    SAUDE = ("Saude")
    JURIDICO = ("Juridico")
    OPERACOES = ("Operacoes")

    def __init__(self, texto: str) -> None:
        self.texto = texto