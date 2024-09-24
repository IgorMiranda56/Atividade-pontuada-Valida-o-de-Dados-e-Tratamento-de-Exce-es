from projeto.models.pessoa_juridica import PessoaJuridica
from projeto.models.endereco import Endereco

#Definindo classe
class Fornecedor(PessoaJuridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricao_estadual: str,
                produto, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, cnpj, inscricao_estadual, endereco)
        self.produto = produto

#Definindo exceção para atributo
    def _verificar_id(self, id: int) -> int:
        return super()._verificar_id(id)

    def _verificar_nome(self, nome: str) -> str:
        return super()._verificar_nome(nome)

#Tostring()
    def __str__(self) -> str:
        return (super().__str__() +
                f"\nProduto: {self.produto}")