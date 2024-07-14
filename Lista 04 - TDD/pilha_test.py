import unittest
from pilha import Pilha

class TestPilha(unittest.TestCase):
    def test_empilhar(self):
        pilha = Pilha()
        pilha.empilhar(1)
        pilha.empilhar(2)
        pilha.empilhar(3)
        self.assertEqual(3, pilha.length())

    def test_desempilhar(self):
        pilha = Pilha()
        pilha.empilhar(1)
        pilha.empilhar(2)
        pilha.desempilhar()
        self.assertEqual(1, pilha.length())

    def test_is_empty(self):
        pilha = Pilha()
        self.assertTrue(pilha.is_empty())

if __name__ == '__main__':
    unittest.main()