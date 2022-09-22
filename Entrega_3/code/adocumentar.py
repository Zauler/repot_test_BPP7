class Areas:
    """Esta clase calcula las áreas de diferentes figuras geométricas
    """

    def areaCuadrado(lado):
        """Calcula el área de un cuadrado
        elevando al cuadrado el lado pasado por parámetro """

        return "El area de cuadrado es: " +str(lado*lado)

    def areaTriangulo(base,altura):
        """Calcula el área de un triángulo 
        utilizando los parametros de base y altura"""

        return "El área del triangulo es: " +str((base*altura)/2)


help(Areas)