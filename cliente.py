from pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome)
        self._cpf = cpf

    def __str__(self):
        return f'nome = {self._nome} sobrenome = {self._sobrenome}'

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf