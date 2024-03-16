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

if __name__ == '__main__':
  unittest.main()