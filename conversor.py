# conversor.py

def fahrenheit_para_celsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius."""
    # Fórmula correta: (F - 32) * 5/9
    return (fahrenheit - 32) * 5.0/9.0

def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit."""
    # Fórmula correta: (C * 9/5) + 32
    return (celsius * 9.0/5.0) + 32