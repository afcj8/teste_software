import unittest
from validar_senha import validar_senha

class TestValidacaoSenha(unittest.TestCase):
    def test_senha_valida(self):
        self.assertTrue(validar_senha("Ab123@78"))
        
    def test_senha_curta(self):
        self.assertFalse(validar_senha("P!a1"))
        
    def test_senha_longa(self):
        self.assertFalse(validar_senha("123456@Kaassfsafasfasr2342352"))
    
    def test_senha_sem_numeros(self):
        self.assertFalse(validar_senha("adsafsaf!Sa"))
        
    def test_so_numeros(self):
        self.assertFalse(validar_senha("12345678"))
        
    def test_numeros_e_minusculo(self):
        self.assertFalse(validar_senha("1234567p"))
        
    def test_numeros_e_maiusculo(self):
        self.assertFalse(validar_senha("1234567P"))

    def test_numeros_e_especial(self):
        self.assertFalse(validar_senha("123456!!"))
    
if __name__ == '__main__':
    unittest.main()