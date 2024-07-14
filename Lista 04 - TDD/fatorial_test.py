import unittest
from fatorial import Factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_positivo(self):
        factorial = Factorial()
        resultado = factorial.factorial_positivo(4)
        self.assertEqual(resultado, 24)

    def test_factorial_zero(self):
        factorial = Factorial()
        resultado = factorial.factorial_zero(0)
        self.assertEqual(resultado, 1)

    def test_factorial_negativo(self):
        factorial = Factorial()
        with self.assertRaises(ValueError):
            resultado = factorial.factorial_negativo(-2)

if __name__ == '__main__':
    unittest.main()