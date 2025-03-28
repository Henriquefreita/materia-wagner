from endereco import endereco
from abc import ABC, abstractmethod
class cliente():
    def __init__(self, nome:str, telefone:int, endereco : endereco, cpf:str,):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf= cpf



