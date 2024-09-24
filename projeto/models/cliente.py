from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.pessoa_fisica import PessoaFisica

#Definindo classe
class Cliente(PessoaFisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Genero, estado_civil: EstadoCivil, data_nascimento: str, 
                protocolo_atendimento: int, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estado_civil, data_nascimento, endereco)
        self.protocolo_atendimento = self._verificar_protocolo_atendimento(protocolo_atendimento)
    
#Definindo exceção para atributo
    def _verificar_id(self, id: int) -> int:
        return super()._verificar_id(id)

    def _verificar_protocolo_atendimento(self, protocolo_atendimento:int) -> int:
        #Método para verificar com duas exceções de CLiente se ele é int e se o numero é positivo.
        if not isinstance(protocolo_atendimento,int):
            raise TypeError("Digite somente numeros inteiros para cliente.")
        if protocolo_atendimento < 0:
            raise ValueError("Digite um numero que seja inteiro e positivo para cliente.")
        return protocolo_atendimento
    
#Tostring()
    def __str__(self) -> str:
        return (super().__str__() +
                f"\nProtocolo Atendimento: {self.protocolo_atendimento}")