import random

class Craps:
  def __init__(self):
    self._soma, self._ponto, self._vencedor = 0, 0, 0
    self._primeiraRodada = True

  def fimDeJogo(self):
    return self._vencedor == 1 or self._vencedor == 2

  @property
  def vencedor(self):
    return self._vencedor

  def _rolarUmDado(self):
    return random.randint(1, 6)
  
  def rolarDados(self):
    self._soma = self._rolarUmDado() + self._rolarUmDado()
    if self._primeiraRodada:
      if self._soma == 7 or self._soma == 11:
        self._vencedor = 1
      elif self._soma == 2 or self._soma == 3 or self._soma == 12:
        self._vencedor = 2
      else:
        self._ponto = self._soma
      self._primeiraRodada = False
    else:
      if self._soma == self._ponto:
        self._vencedor = 1
      elif self._soma == 7:
        self._vencedor = 2
    return self._soma