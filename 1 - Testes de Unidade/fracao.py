def mmc(a, b):
  cont = 2
  res = 1
    
  while a + b != 2:
    if a % cont == 0 or b % cont == 0:
      res *= cont
      if a % cont == 0:
        a //= cont
      if b % cont == 0:
        b //= cont
    else:
      cont += 1
          
  return res

class Fracao:
  def __init__(self, n, d):
    if (not isinstance(n, int)) or (not isinstance(d, int)):
      raise TypeError('Parametros devem ser do tipo inteiro')
    if d == 0:
      raise ValueError('Denominador deve ser diferente de zero')
    self._numerador = n
    self._denominador = d

  @property
  def numerador(self):
    return self._numerador
 
  @property
  def denominador(self):
    return self._denominador
  
  def __eq__(self, other):
    if not isinstance(other, Fracao):
        return False
    return self.numerador == other.numerador and self.denominador == other.denominador
  
  def multiplicacao(self, f):
    n = self.numerador * f.numerador
    d = self.denominador * f.denominador
    return Fracao(n, d)
  
  def divisao(self, f):
    n = self.numerador * f.denominador
    d = self.denominador * f.numerador
    return Fracao(n, d)
  
  def mmc(self, f):
    a = self.denominador
    b = f.denominador
    return mmc(a, b)
  
  def adicao(self, f):
    if self.denominador == f.denominador:
      n = self.numerador + f.numerador
      d = self.denominador
    else:
      d = self.mmc(f)
      n1 = self.numerador * (d // self.denominador)
      n2 = f.numerador * (d // f.denominador)
      n = n1 + n2
    return Fracao(n, d)