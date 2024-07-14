import unittest

def factorial(n):
    if (n == 0):    # Caso de base
        return 1
    else:
        fat = n * factorial(n - 1)
        return fat
    
class Factorial:
    def factorial(self, n):
        return factorial(n)
    
    def factorial_positivo(self, n):
        return factorial(n)
    
    def factorial_zero(self, n):
        return factorial(n)
    
    def factorial_negativo(self, n):
        if n < 0:
            raise ValueError('Não existe fatorial de número negativo')