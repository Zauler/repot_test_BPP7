###ACTIVIDAD LECCIÓN 2 COMPRENDER LA IMPORTANCIA DEL DESARROLLO GUIADO POR PRUEBAS
##IMPORTACIONES

import unittest
from funciones import sumanumeros,area
from math import pi


##TEST

#Función sumanumeros:

class TestSum(unittest.TestCase):
    def test_sumanumeros_arg_defecto(self):
        """
        Test de argumentos por defecto
        """
        self.assertEqual(sumanumeros(),5050)
        self.assertEqual(sumanumeros(numbers=None),5050)

    def test_suma_numeros_varios_inputs(self):
        """
        test de varios valores y formatos
        """
        self.assertEqual(sumanumeros(range(1,11)), 55)
        self.assertEqual(sumanumeros([1,2,3]), 6)
        self.assertEqual(sumanumeros((1,2,3)), 6)
        self.assertEqual(sumanumeros([]),0)



#Función area:

class TestArea(unittest.TestCase):
    def test_areas(self):
        """
        Test de datos conocidos
        """
        self.assertAlmostEqual(area(1),pi)
        self.assertAlmostEqual(area(0),0)
        self.assertAlmostEqual(area(3),pi*(3**2))

    def testerrornegativos(self):
        """
        Test de valores negativos
        """
        self.assertRaises(ValueError,area,-1) #Se indica el error que debería dar, la función y el valor que sabes que da el error

    def test_tipos(self):
        """
        Test de valores con cadenas de texto
        """
        self.assertRaises(TypeError,area,"pepe") #cadena de texto
        self.assertRaises(TypeError,area,True) #booleano
        self.assertRaises(TypeError,area,2+3j) #numero imaginario
    
        

#Para utilizar el test se tiene que estar en la carpeta del test y escribir en la consola: python -m unittest -v test_unittest
