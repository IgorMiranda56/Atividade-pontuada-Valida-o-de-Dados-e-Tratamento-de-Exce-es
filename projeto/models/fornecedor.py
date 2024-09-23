from projeto.models.endereco import Endereco
from projeto.models.pessoa_juridica import PessoaJuridica

#Definindo Classes
class Fornecedor(PessoaJuridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricao_estadual: str, produto: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, cnpj, inscricao_estadual, endereco)
        self.produto = produto

#Tostring()
    def __str__(self) -> str:
        return (super().__str__(),
                f"\nProduto: {self.produto}")