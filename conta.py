from cliente import Cliente
from data import Data


class Conta:

    def __init__(self, numero, titular: Cliente, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._data_abertura = Data().data()

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if self._saldo + self._limite < valor:
            return False
        self._saldo -= valor
        return True

    def extrato(self):
        _dataCorrente = Data().data()
        print("-"*25)
        print(
            f"Nome Completo: {self._titular.nome} {self._titular.sobrenome} \n"
            f"CPF: {self._titular.cpf} \nNúmero da Conta: {self._numero} \n"
            f"Saldo Atual: {self._saldo} \n"
            f"Data de Abertura da Conta: {self._data_abertura} \n"
            f"Data de emissão do extrato: {_dataCorrente}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou:
            destino.deposita(valor)
            return True
        return False


