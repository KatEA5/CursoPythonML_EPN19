"""
Esta e sla librería de areas de figuras geometricas
Autor:
Fecha: 21/agosto/2019
Observaciones:
"""

from math import pi, pow


def circulo(radio):
    """
    Esta funcion devuelve el area de un circulo de radio r
    :param radio: es un numero real
    :return: area como numero real
    """
    area = pi*pow(radio,2)
    return area


def rectangulo(lado1, lado2):
    area = lado1*lado2
    return area


def triangulo (base, altura):
    area = base*altura/2