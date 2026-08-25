# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:11:08 2026

@author: gabri

Reto 5: Picas y fijas
El juego de las Picas y Fijas es un juego matemático muy sencillo, consiste en adivinar un número de 4 cifras y de todos los dígitos diferentes. Para esto, el jugador que intenta adivinar deberá decir el número que cree está escondiendo el otro, y este deberá responder el número de picas y fijas que tiene ahora el jugador.
Una pica es un dígito que se encuentra en el número a adivinar, pero no está en el lugar correcto; y una fija es un dígito correctamente colocado.
Por ejemplo, si el número secreto es 1234 y el otro jugador dice 1325, tendrá dos picas y una fija.
Debes crear una función que devuelva un diccionario con las llaves "PICAS" y "FIJAS" que represente el resultado de la jugada si un jugador trata de adivinar el numero_secreto con el número intento.
Tu solución debe tener una función de acuerdo con la siguiente especificación:
Nombre de la función: picas_y_fijas
Si lo requieres, puedes agregar funciones adicionales.
Descripción de parámetros:
Nombre|Tipo|Descripción
numero_secreto|int|Número por adivinar.
intento|int|Número con el cual se intenta adivinar.
Descripción del retorno:
Tipo|Descripción|dict
Diccionario con las llaves "PICAS" y "FIJAS" que describen el resultado del intento.
"""

#picas y fijas
def picas_y_fijas(numero_secreto: int, intento: int) -> dict:
    secreto = str(numero_secreto)
    intento = str(intento)

    picas = 0
    fijas = 0

    for i in range(4):
        if intento[i] == secreto[i]:
            fijas += 1
        elif intento[i] in secreto:
            picas += 1

    resultado = {
        "PICAS": picas,
        "FIJAS": fijas
    }
    return resultado
    
##Principal
numero_secreto= int(input("Ingresa el numero secreto de 4 cifras(Número por adivinar.):"))
intento= int(input("Número con el cual se intenta adivinar:"))
resultado =picas_y_fijas(numero_secreto, intento)

print(resultado)