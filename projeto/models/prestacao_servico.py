from projeto.models.endereco import Endereco
from projeto.models.pessoa_juridica import PessoaJuridica

#Definindo classe
class PrestacaoServacao(PessoaJuridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricao_estadual: str, contrato_inicio: str, contrato_fim: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, cnpj, inscricao_estadual, endereco)
        self.contrato_inicio = contrato_inicio
        self.contrato_fim = contrato_fim

#Tostring()
    def __str__(self) -> str:
        return (super().__str__(),
                f"\nInicio do Contrato: {self.contrato_inicio}"
                f"\nFim do contrato: {self.contrato_fim}")