# Este programa está en el archivo casa.py

def area_cuadrado(lado: int)-> int:
    """
       Calcula el área de un cuadrado dada la medida de su lado
    """
    return lado * lado


def area_triangulo(base: int, altura: int)-> float:
    """
        Calcula el área de un triángulo dada la medida de la base y de la altura.
    """   
    return (base * altura) / 2


def area_casa(frente: int, techo: int)-> float:
    """
        Calcula el área del dibujo de una casa que se forma con un cuadrado
        y un triángulo encima (el techo).
        El frente de la casa será igual al lado del cuadrado y a la base del triángulo.
        La altura del techo será la altura del triángulo.
    """
    cuadrado = area_cuadrado(frente)
    triangulo = area_triangulo(frente, techo)
    return cuadrado + triangulo
    
medida_frente = 7
medida_techo = 5
resultado = area_casa(medida_frente, medida_techo)
print("El área de una casa con", medida_frente, "metros de frente y un techo de",
       medida_techo, "metros de alto es ", round(resultado, 2), "metros")