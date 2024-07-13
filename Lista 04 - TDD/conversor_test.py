import unittest
from conversor import Conversor

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        conversor = Conversor()
        resultado = conversor.convert_celsius_to_fahrenheit(10)
        self.assertEqual(resultado, 50)

    def test_fahrenheit_to_celsius(self):
        conversor = Conversor()
        resultado = conversor.convert_fahrenheit_to_celsius(50)
        self.assertEqual(resultado, 10)

if __name__ == '__main__':
    unittest.main()