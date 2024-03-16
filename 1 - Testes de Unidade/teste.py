import unittest
from fracao import Fracao

class FracaoTest(unittest.TestCase):

  def test_Fracao_ok(self):
    Fracao(1, 2)
 
  def test_Fracao_bad_type_numerador(self):
    with self.assertRaises(TypeError):
        Fracao('1', 2)

  def test_Fracao_bad_type_denominador(self):
    with self.assertRaises(TypeError):
        Fracao(1, '2')

  def test_Fracao_denominador_zero(self):
    with self.assertRaises(ValueError):
        Fracao(1, 0)

  def test_eq(self):
    f1 = Fracao(1, 2)
    f2 = Fracao(1, 2)
    f3 = Fracao(3, 5)
    
    self.assertEqual(f1, f1)
    self.assertEqual(f1, f2)
    self.assertNotEqual(f1, f3) 

  def test_multiplicacao(self):
    f1 = Fracao(1, 2)
    f2 = Fracao(3, 5)
    resultado = f1.multiplicacao(f2)
    
    self.assertEqual(Fracao(3, 10), resultado)

  def test_divisao(self):
    f1 = Fracao(3, 4)
    f2 = Fracao(5, 2)
    resultado = f1.divisao(f2)

    self.assertEqual(Fracao(6, 20), resultado)

  def test_adicao(self):
    f1 = Fracao(5, 8)
    f2 = Fracao(1, 4)
    resultado = f1.adicao(f2)

    self.assertEqual(Fracao(7, 8), resultado)

  def test_subtracao(self):
    f1 = Fracao(5, 8)
    f2 = Fracao(2, 4)
    resultado = f1.subtracao(f2)

    self.assertEqual(Fracao(1, 8), resultado)

if __name__ == '__main__':
  unittest.main()