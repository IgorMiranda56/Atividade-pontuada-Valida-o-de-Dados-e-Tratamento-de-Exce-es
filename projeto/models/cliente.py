from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.pessoa_fisica import PessoaFisica

#Definindo classes
class Cliente(PessoaFisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, genero: Genero, estado_civil: EstadoCivil, dataNascimento: str,
                 protocolo_atendimento: int, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, genero, estado_civil, dataNascimento, endereco)
        self.protocolo_atendimento = self._verificar_protocolo(protocolo_atendimento)

#Definindo exceção para atributo
    def _verificar_verificar_protocolo(self, protocolo_atendimento):
        if not isinstance(protocolo_atendimento, int):
            raise TypeError("Protocolo de atendimento somente pode conter numeros.")
        return protocolo_atendimento

#Tostring()
    def __str__(self) -> str:
        return (super().__str__(),
                f"\nProcolo de Atendimento: {self.protocolo_atendimento}")