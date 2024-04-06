import desconto
import unittest

class TestDesconto(unittest.TestCase):
    def test_idade_dependente_invalida(self):
        # Casos de teste para idade do dependente inválida
        self.assertEqual(desconto.calcular_desconto(300, -1), "Idade do dependente inválida")  
        self.assertEqual(desconto.calcular_desconto(300, 25), "Idade do dependente inválida")  

    def test_valor_compra_abaixo_minimo(self):
        # Casos de teste para valor da compra abaixo do mínimo
        self.assertEqual(desconto.calcular_desconto(249, 10), "Valor da compra abaixo do mínimo")  

    def test_desconto(self):
        # Casos de teste para desconto baseado na idade do dependente
        self.assertEqual(desconto.calcular_desconto(300, 8), 45.0) 
        self.assertEqual(desconto.calcular_desconto(400, 16), 48.0) 
        self.assertEqual(desconto.calcular_desconto(500, 20), 25.0)  
        self.assertEqual(desconto.calcular_desconto(600, 22), 18.0)  

    def test_valores_limites(self):
        # Casos de teste para valores limites
        self.assertEqual(desconto.calcular_desconto(250, 0), 37.5)  
        self.assertEqual(desconto.calcular_desconto(250, 12), 37.5) 
        self.assertEqual(desconto.calcular_desconto(250, 24), 7.5)
        self.assertEqual(desconto.calcular_desconto(1000, 0), 150.0) 
        self.assertEqual(desconto.calcular_desconto(1000, 24), 30.0) 

if __name__ == '__main__':
    unittest.main()