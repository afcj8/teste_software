import unittest
from craps import Craps
from unittest.mock import Mock
import random

class CrapsTest(unittest.TestCase):

  def test_jogador_perde_de_primeira(self):
    random.randint = Mock()
    random.randint.return_value = 6
 	
    c = Craps()
    c.rolarDados()

    self.assertTrue(c.fimDeJogo())
    self.assertEqual(2, c.vencedor)

  def test_jogador_ganha_de_primeira(self):
    random.randint = Mock()
    random.randint.side_effect = [5, 2]

    c = Craps()
    c.rolarDados()

    self.assertTrue(c.fimDeJogo())
    self.assertEqual(1, c.vencedor)

  def test_jogador_perde_de_terceira(self):
    c = Craps()
    random.randint = Mock()
    # primeira rodada
    random.randint.side_effect = [3, 5]
    c.rolarDados()
    self.assertFalse(c.fimDeJogo())
    # segunda rodada
    random.randint.side_effect = [6, 5]
    c.rolarDados()
    self.assertFalse(c.fimDeJogo())
    # terceira rodada
    random.randint.side_effect = [5, 2]
    c.rolarDados()
    self.assertTrue(c.fimDeJogo())
    self.assertEqual(2, c.vencedor)

if __name__ == '__main__':
  unittest.main()