import unittest
from saldo_insuficiente_exception import SaldoInsuficienteException

class Conta:
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException('Saldo insuficiente!')
        self.saldo = self.saldo - valor
        return self.saldo

    def consultar_saldo(self):
        return self.saldo