"""
Este script hace ........
Autor: LGFE
Fecha: 06/06/06
"""

#%%
import numpy as np
from math import pow, pi, sqrt
import pandas as pd

#%%
def circle_area(radio):
    """
    Esta funcion devuelve el area de un circulo de radio r
    :param radio: es un numero real
    :return: area como numero real
    """
    area = pi*pow(radio,2)
    return area

def hipotenusa(cateto_1, cateto_2):
    """
    Esta funcion calcula la hipo de un triag rect
    :param cateto_1:
    :param cateto_2:
    :return:
    """
    hip = sqrt(cateto_1**2+cateto_2**2)
    return hip

def main():
    # area_1 = circle_area(radio=2.5)
    # area_2 = circle_area(radio=3.0)
    cateto_1 = 1.0
    cateto_2 = 1.0
    hip1 = hipotenusa(cateto_1=cateto_1,cateto_2=cateto_2)
    area = circle_area(radio=hip1/2)
    print('Area de un circulo de diametro {} es {}'.format(hip1, area))
    print('Hipotenusa de {} y {} es {}'.format(cateto_1, cateto_2, hip1))


if __name__ == '__main__':
    main()


#%%

def main():
    arae_