from projeto.models.pessoa_juridica import PessoaJuridica
from projeto.models.endereco import Endereco

#Definindo classe
class PrestacaoServico(PessoaJuridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricao_estadual: str,
                contrato_inicio: str, contrato_fim: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, cnpj, inscricao_estadual, endereco)
        self.contrato_inicio = contrato_inicio
        self.contrato_fim = contrato_fim

#Definindo exceção para atributo
    def _verificar_id(self, id: int) -> int:
        return super()._verificar_id(id)

    def _verificar_nome(self, nome: str) -> str:
        return super()._verificar_nome(nome)
    
#Tostring()
    def __str__(self) -> str:
        return (super().__str__() +
                f"\nContrato Inicio: {self.contrato_inicio}"
                f"\nContrato Fim: {self.contrato_fim}")