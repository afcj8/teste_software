import unittest
from conta import Conta
from saldo_insuficiente_exception import SaldoInsuficienteException

class TestConta(unittest.TestCase):
    
    def test_criacao_conta(self):
        conta = Conta(123, 456, 1000)
        self.assertEqual(conta.numero, 123)
        self.assertEqual(conta.agencia, 456)
        self.assertEqual(conta.saldo, 1000)
    
    def test_deposito(self):
        conta = Conta(123, 456, 1000)
        conta.depositar(500)
        self.assertEqual(conta.consultar_saldo(), 1500)
    
    def test_saque(self):
        conta = Conta(123, 456, 1000)
        conta.sacar(500)
        self.assertEqual(conta.consultar_saldo(), 500)
    
    def test_saque_saldo_insuficiente(self):
        conta = Conta(123, 456, 1000)
        with self.assertRaises(SaldoInsuficienteException):
            conta.sacar(1500)
    
    def test_saldo_negativo(self):
        conta = Conta(123, 456, 1000)
        with self.assertRaises(SaldoInsuficienteException):
            conta.sacar(2000)

if __name__ == '__main__':
    unittest.main()