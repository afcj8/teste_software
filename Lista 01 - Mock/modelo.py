import datetime

class DAOCompra:
  
  def __init__(self):
    self._placa = None
    self._compra = False
    self._dataCompra = None
  
  def getUltimaData(self, placa):
    return None
  
  def setDataCompra(self, data):
     self._dataCompra = data
  
  def setPlacaCompra(self, placa):
    self._placa = placa
    self._compra = True
    
  def save(self, placa, data):
     self.setPlacaCompra(placa)
     self.setDataCompra(data)

class DAOVenda:
  def getUltimaData(self, placa):
    return None
 
class ServicoVeiculo:
  def __init__(self):
    self.daoCompra = DAOCompra()
    self.daoVenda = DAOVenda()
  
  def isEmPosseDaLoja(self, placa):
    ultima_compra = self.daoCompra.getUltimaData(placa)
    ultima_venda = self.daoVenda.getUltimaData(placa)
    if ultima_compra is None and ultima_venda is None:
      return False
    elif ultima_compra is not None and ultima_venda is None:
      return True
    return ultima_venda < ultima_compra 
 
  def compra(self, placa, data):
    if self.isEmPosseDaLoja(placa) == False:
       self.daoCompra.save(placa, data)       
       return True
    else:
       return False