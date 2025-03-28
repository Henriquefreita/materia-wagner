from cliente import cliente
class endereco(cliente):
    def __init__(self,cep: int, rua: str, bairro: int, cidade: str):
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
    def _str_(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereco}"