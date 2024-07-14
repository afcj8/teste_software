import unittest

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, n):
        self.itens.append(n)

    def desempilhar(self):
        self.itens.pop(len(self.itens) - 1)

    def is_empty(self):
        return len(self.itens) == 0
    
    def length(self):
        return len(self.itens)