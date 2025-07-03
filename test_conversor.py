
import unittest
from conversor import fahrenheit_para_celsius, celsius_para_fahrenheit

class TestConversor(unittest.TestCase):

    def test_fahrenheit_para_celsius(self):
        """Testa a conversão de Fahrenheit para Celsius com valores conhecidos."""
        # Teste 1: Ponto de congelamento da água
        self.assertAlmostEqual(fahrenheit_para_celsius(32), 0)
        # Teste 2: Ponto de ebulição da água
        self.assertAlmostEqual(fahrenheit_para_celsius(212), 100)

    def test_celsius_para_fahrenheit(self):
        """Testa a conversão de Celsius para Fahrenheit com valores conhecidos."""
        # Teste 3: Zero absoluto (aproximado)
        self.assertAlmostEqual(celsius_para_fahrenheit(0), 32)
        # Teste 4: Temperatura corporal humana média
        self.assertAlmostEqual(celsius_para_fahrenheit(37), 98.6)

if __name__ == '__main__':
    unittest.main()