import unittest
import triangulo

class TestTriangulo(unittest.TestCase):
    def test_validar_forma(self):

        self.assertTrue(triangulo.Triangulo(2, 6, 5).validarForma())  # Triângulo válido
        self.assertTrue(triangulo.Triangulo(4, 4, 4).validarForma())  # Triângulo válido
        self.assertTrue(triangulo.Triangulo(5, 3, 7).validarForma())  # Triângulo válido

        self.assertFalse(triangulo.Triangulo(6, 2, 4).validarForma())   # Triângulo inválido
        self.assertFalse(triangulo.Triangulo(2, 3, 8).validarForma())   # Triângulo inválido
        self.assertFalse(triangulo.Triangulo(0, 2, 5).validarForma())   # Triângulo inválido
        self.assertFalse(triangulo.Triangulo(-6, 2, 7).validarForma())  # Triângulo inválido

    def test_eh_equilatero(self):

        self.assertTrue(triangulo.Triangulo(5, 5, 5).ehEquilatero())   # Triângulo Equilátero
        self.assertFalse(triangulo.Triangulo(4, 5, 2).ehEquilatero())  # Triângulo não é Equilátero
        self.assertFalse(triangulo.Triangulo(5, 5, 4).ehEquilatero())  # Triângulo não é Equilátero
        self.assertFalse(triangulo.Triangulo(3, 5, 3).ehEquilatero())  # Triângulo não é Equilátero
        self.assertFalse(triangulo.Triangulo(4, 5, 5).ehEquilatero())  # Triângulo não é Equilátero

    def test_eh_isosceles(self):

        self.assertTrue(triangulo.Triangulo(5, 5, 7).ehIsosceles())  # Triângulo Isósceles
        self.assertTrue(triangulo.Triangulo(5, 7, 7).ehIsosceles())  # Triângulo Isósceles
        self.assertTrue(triangulo.Triangulo(7, 5, 7).ehIsosceles())  # Triângulo Isósceles
        self.assertFalse(triangulo.Triangulo(4, 5, 3).ehIsosceles())  # Triângulo não é Isósceles
        self.assertFalse(triangulo.Triangulo(3, 4, 5).ehIsosceles())  # Triângulo não é Isósceles

    def test_eh_escaleno(self):

        self.assertTrue(triangulo.Triangulo(3, 4, 5).ehEscaleno())  # Triângulo Escaleno
        self.assertFalse(triangulo.Triangulo(5, 5, 5).ehEscaleno())  # Triângulo não é Escaleno
        self.assertFalse(triangulo.Triangulo(5, 5, 2).ehEscaleno())  # Triângulo não é Escaleno
        self.assertFalse(triangulo.Triangulo(5, 2, 5).ehEscaleno())  # Triângulo não é Escaleno
        self.assertFalse(triangulo.Triangulo(2, 5, 5).ehEscaleno())  # Triângulo não é Escaleno

    def test_valores_limites(self):
        # Casos de teste para valores mínimos
        self.assertTrue(triangulo.Triangulo(10, 10, 10).validarForma())
        self.assertTrue(triangulo.Triangulo(10, 10, 10).ehEquilatero())
        self.assertTrue(triangulo.Triangulo(1, 10, 10).ehIsosceles()) 
        self.assertTrue(triangulo.Triangulo(2, 3, 4).ehEscaleno())  

        # Casos de teste para valores máximos
        self.assertTrue(triangulo.Triangulo(100, 100, 100).validarForma())  
        self.assertTrue(triangulo.Triangulo(100, 100, 100).ehEquilatero())  
        self.assertFalse(triangulo.Triangulo(50, 90, 100).ehIsosceles())  
        self.assertFalse(triangulo.Triangulo(75, 100, 75).ehEscaleno())  

        # Casos de teste para valores extremos
        self.assertTrue(triangulo.Triangulo(50, 51, 51).validarForma())  
        self.assertFalse(triangulo.Triangulo(50, 51, 51).ehEquilatero())  
        self.assertTrue(triangulo.Triangulo(50, 51, 51).ehIsosceles())  
        self.assertFalse(triangulo.Triangulo(50, 51, 51).ehEscaleno())  

        # Casos de teste para valores nulos ou negativos
        self.assertFalse(triangulo.Triangulo(0, 10, 12).validarForma())  
        self.assertFalse(triangulo.Triangulo(0, 10, 12).ehEquilatero())  
        self.assertFalse(triangulo.Triangulo(0, 10, 12).ehIsosceles())  
        self.assertFalse(triangulo.Triangulo(0, 10, 12).ehEscaleno())  

        self.assertFalse(triangulo.Triangulo(-10, 2, 3).validarForma())  
        self.assertFalse(triangulo.Triangulo(-10, 2, 3).ehEquilatero())  
        self.assertFalse(triangulo.Triangulo(-10, 2, 3).ehIsosceles())  
        self.assertFalse(triangulo.Triangulo(-10, 2, 3).ehEscaleno())  

if __name__ == '__main__':
    unittest.main()