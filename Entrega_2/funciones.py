###ACTIVIDAD LECCIÓN 2 COMPRENDER LA IMPORTANCIA DEL DESARROLLO GUIADO POR PRUEBAS
##IMPORTACIONES

from math import pi


##FUNCIONES

#Función sumanumeros:

def sumanumeros(numbers=None):
    if numbers is None:
        return sum(range(1,101))
    return sum(numbers)


#Función area:

def area(r):
    if r<0:
        raise ValueError("No existen areas negativas,introduzca valor positivo")
    if type(r) not in [float,int]:
        raise TypeError ("Por favor introduzca un número positivo")

    areaC=pi*(r**2)
    return areaC

