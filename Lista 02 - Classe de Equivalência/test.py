# test.py

import unittest
import modelo

class TestTriangulo(unittest.TestCase):

    def test_validar_forma(self):

        self.assertTrue(modelo.Triangulo(2, 6, 5).validarForma())  # Triângulo válido
        self.assertTrue(modelo.Triangulo(4, 4, 4).validarForma())  # Triângulo válido
        self.assertTrue(modelo.Triangulo(5, 3, 7).validarForma())  # Triângulo válido

        self.assertFalse(modelo.Triangulo(6, 2, 4).validarForma())   # Triângulo inválido
        self.assertFalse(modelo.Triangulo(2, 3, 8).validarForma())   # Triângulo inválido
        self.assertFalse(modelo.Triangulo(0, 2, 5).validarForma())   # Triângulo inválido
        self.assertFalse(modelo.Triangulo(-6, 2, 7).validarForma())  # Triângulo inválido

    def test_eh_equilatero(self):

        self.assertTrue(modelo.Triangulo(5, 5, 5).ehEquilatero())   # Triângulo Equilátero
        self.assertFalse(modelo.Triangulo(4, 5, 2).ehEquilatero())  # Triângulo não é Equilátero
        self.assertFalse(modelo.Triangulo(5, 5, 4).ehEquilatero())  # Triângulo não é Equilátero
        self.assertFalse(modelo.Triangulo(3, 5, 3).ehEquilatero())  # Triângulo não é Equilátero
        self.assertFalse(modelo.Triangulo(4, 5, 5).ehEquilatero())  # Triângulo não é Equilátero

    def test_eh_isosceles(self):

        self.assertTrue(modelo.Triangulo(5, 5, 7).ehIsosceles())  # Triângulo Isósceles
        self.assertTrue(modelo.Triangulo(5, 7, 7).ehIsosceles())  # Triângulo Isósceles
        self.assertTrue(modelo.Triangulo(7, 5, 7).ehIsosceles())  # Triângulo Isósceles
        self.assertFalse(modelo.Triangulo(3, 3, 3).ehIsosceles())  # Triângulo não é Isósceles
        self.assertFalse(modelo.Triangulo(3, 4, 5).ehIsosceles())  # Triângulo não é Isósceles

    def test_eh_escaleno(self):

        self.assertTrue(modelo.Triangulo(3, 4, 5).ehEscaleno())  # Triângulo Escaleno
        self.assertFalse(modelo.Triangulo(5, 5, 5).ehEscaleno())  # Triângulo não é Escaleno
        self.assertFalse(modelo.Triangulo(5, 5, 2).ehEscaleno())  # Triângulo não é Escaleno
        self.assertFalse(modelo.Triangulo(5, 2, 5).ehEscaleno())  # Triângulo não é Escaleno
        self.assertFalse(modelo.Triangulo(2, 5, 5).ehEscaleno())  # Triângulo não é Escaleno

if __name__ == '__main__':
    unittest.main()