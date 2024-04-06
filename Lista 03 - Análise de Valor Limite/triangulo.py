import datetime

class Triangulo:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validarForma(self):
        if (self.a < (self.b + self.c)):
            if (self.b < (self.a + self.c)):
                if (self.c < (self.a + self.b)):
                    if (self.a > 0 and self.b > 0 and self.c > 0):
                        return True
        return False

    # Triângulo Equilátero: três lados iguais;
    def ehEquilatero(self):
        if (self.validarForma()):
            if (self.a == self.b and self.a == self.c):
                return True
        return False

    # Triângulo Isósceles: quaisquer dois lados iguais;
    def ehIsosceles(self):
        if(self.validarForma()):
            if (self.a == self.b or self.a == self.c or self.b == self.c):
                return True
        return False

    # Triângulo Escaleno: três lados diferentes;
    def ehEscaleno(self):
        if(self.validarForma()):
            if (self.a != self.b and self.a != self.c and self.b != self.c):
                return True
        return False