###ACTIVIDAD LECCIÓN 2 COMPRENDER LA IMPORTANCIA DEL DESARROLLO GUIADO POR PRUEBAS
##IMPORTACIONES

import pytest   
from funciones import sumanumeros,area
from math import pi


##TEST

#Función sumanumeros:

def test_sumanumeros_por_defecto():
    """
    Test probando función por defecto vacía
    """
    suma=sumanumeros()
    assert suma == 5050

def test_sumanumeros_por_defecto_none():
    """
    Test probando función por defecto especificando None
    """
    suma=sumanumeros(numbers=None)
    assert suma == 5050

def test_suma_numeros_inputs_1():
    """
    Test probando la función con valores
    """
    suma=sumanumeros(range(1,11))
    assert suma == 55

def test_suma_numeros_inputs_2_lista():
    """
    Test probando la función con una lista
    """
    suma=sumanumeros([1,2,3])
    assert suma == 6

def test_suma_numeros_inputs_3_tupla():
    """
    Test probando la función con una tupla
    """
    suma=sumanumeros((1,2,3))
    assert suma == 6

def test_suma_numeros_inputs_4_listavacia():
    """
    Test probando la función con una lista vacía
    """
    suma  = sumanumeros([])
    assert suma == 0


#Función area:

def test_area_valores_1():
    """
    Test probando los valores cuando se introduce un caso simple
    """
    calculo = area(1)
    assert calculo == pi   

def test_area_valores_2():
    """
    Test en el límite
    """
    calculo = area(0)
    assert calculo == 0 

def test_area_valores_3():
    """
    Test probando los valores cuando se introduce un caso cualquiera
    """

    calculo = area(3)
    assert calculo == pi*(3**2)



def test_area_exception_1():
    """
    Test excepción 1, valores negativos 
    """
    with pytest.raises(ValueError):
        area(-1)

def test_area_exception_2():
    """
    Test excepción 2, cadenas de texto
    """
    with pytest.raises(TypeError):
        area("pepe")


def test_area_exception_3():
    """
    Test excepción 3, booleanos
    """
    with pytest.raises(TypeError):
        area(True)

def test_area_exception_4():
    """
    Test excepción 4, Numeros complejos
    """
    with pytest.raises(TypeError):
        area(2+3j)      


#Para ejecución hace falta estar en la carpeta donde esté este archivo y escribir: pytest -v 