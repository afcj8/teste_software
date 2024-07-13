import unittest

class Conversor:
    def convert_celsius_to_fahrenheit(self, celsius):
        resultado = celsius * 1.8 + 32
        return resultado
    
    def convert_fahrenheit_to_celsius(self, fahrenheit):
        resultado = (fahrenheit - 32) / 1.8
        return resultado