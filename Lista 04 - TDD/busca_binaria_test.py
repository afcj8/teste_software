import unittest
from busca_binaria import BuscaBinaria

class TestBuscaBinaria(unittest.TestCase):
    def test_encontrado(self):
        busca = BuscaBinaria()
        arr = [1, 2, 3, 4]
        self.assertTrue(busca.busca_binaria(arr, 3))

    def test_nao_encontrado(self):
        busca = BuscaBinaria()
        arr = [1, 2, 3, 4]
        self.assertFalse(busca.busca_binaria(arr, 5))

if __name__ == '__main__':
    unittest.main()