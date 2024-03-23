import unittest
from unittest.mock import Mock
import modelo, datetime

class ServicoVeiculoTest(unittest.TestCase):

  def setUp(self):
    self.servico = modelo.ServicoVeiculo()
    self.servico.daoCompra = Mock()
    self.servico.daoVenda = Mock()

  def test_isEmPosseDaLoja_1(self):
    # teste: sem data de compra e venda

    servico = modelo.ServicoVeiculo()
    servico.daoCompra = Mock()
    servico.daoVenda = Mock()

    placa = "NNX2015"
    servico.daoCompra.getUltimaData.return_value = None
    servico.daoVenda.getUltimaData.return_value = None
    em_posse = servico.isEmPosseDaLoja(placa)

    self.assertFalse(em_posse)
    
  def test_isEmPosseDaLoja_2(self):
    # teste: com data de compra e sem data de venda
    
    placa = "NNX2015"

    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = None
    em_posse = self.servico.isEmPosseDaLoja(placa)

    self.assertTrue(em_posse)
    
  def test_isEmPosseDaLoja_3(self):
    # teste: data de compra é anterior à data de venda
    
    placa = "NNX2015"

    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = datetime.datetime(2022, 10, 22)
    em_posse = self.servico.isEmPosseDaLoja(placa)

    self.assertFalse(em_posse)
     
  def test_isEmPosseDaLoja_4(self):
    # teste: data de compra é posterior à data de venda
    
    placa = "NNX2015"
    
    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = datetime.datetime(2021, 10, 22)
    em_posse = self.servico.isEmPosseDaLoja(placa)
    
    self.assertTrue(em_posse)   

  def test_compra_sucesso_1(self):
    # Teste de compra bem-sucedida: sem registro de compra e venda

    placa = "NNX2015"
    data_compra = datetime.datetime(2024, 3, 21)

    self.servico.daoCompra.getUltimaData.return_value = None
    self.servico.daoVenda.getUltimaData.return_value = None
    resultado = self.servico.compra(placa, data_compra)

    self.assertTrue(resultado)
    self.servico.daoCompra.save.assert_called_once_with(placa, data_compra)

  def test_compra_sucesso_2(self):
    # Teste de compra bem-sucedida: data de venda posterior a data de compra

    placa = "NNX2015"
    data_compra = datetime.datetime(2022, 3, 21)
    data_venda = datetime.datetime(2023, 3, 21)

    self.servico.daoCompra.getUltimaData.return_value = data_compra
    self.servico.daoVenda.getUltimaData.return_value = data_venda
    resultado = self.servico.compra(placa, data_compra)

    self.assertTrue(resultado)

  def test_compra_falha_1(self):
    # Teste de compra falha: com registro de compra

    placa = "NNX2015"
    data_compra = datetime.datetime(2022, 3, 21)

    self.servico.daoCompra.getUltimaData.return_value = data_compra
    self.servico.daoVenda.getUltimaData.return_value = None
    resultado = self.servico.compra(placa, data_compra)

    self.assertFalse(resultado)

  def test_compra_falha_2(self):
    # Teste de compra falha: data de compra posterior a data de venda

    placa = "NNX2015"
    data_compra = datetime.datetime(2022, 3, 21)
    data_venda = datetime.datetime(2021, 3, 21)

    self.servico.daoCompra.getUltimaData.return_value = data_compra
    self.servico.daoVenda.getUltimaData.return_value = data_venda
    resultado = self.servico.compra(placa, data_compra)

    self.assertFalse(resultado)

if __name__ == '__main__':
  unittest.main()