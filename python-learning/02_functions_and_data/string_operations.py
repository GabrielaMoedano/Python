# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:30:30 2026

@author: gabri
"""

def funcion (cad1: str, cad2: str)-> int:
    if cad1 == cad2:
        resp = 1
    elif cad1.lower() == str.lower(cad2):
        resp = 2
    else:
        resp = 0
    return resp

def mas_a (c1: str,c2: str, c3: str, c4: str)-> str:
    letra ='a'
    cadena_mas = c1
    cantidad_mas = c1.lower().count(letra)
    
    if c2.lower().count(letra) > cantidad_mas:
        cadena_mas =c2
        cantidad_mas = c2.lower().count(letra)
        
    if c3.lower().count(letra) > cantidad_mas:
        cadena_mas =c3
        cantidad_mas = c3.lower().count(letra)
    if c4.lower().count(letra) > cantidad_mas:
        cadena_mas =c4
        cantidad_mas = c4.lower().count(letra)
        
    return cadena_mas    

""">>>>>>Reto 4: Materias favoritas
Pedro es un estudiante inteligente pero desinteresado por algunas de sus materias. A Pedro le gustan las clases en las que aprende programación, matemática, filosofía y literatura. Por lo anterior, cualquier materia que lleve en su título alguna de estas palabras, será de su agrado.
Pedro está planeando su horario, pero ha puesto a su asistente digital a que le dé posibles conjuntos de tres materias para inscribir en su semestre. Él quiere saber, dados los títulos de las tres materias, cuántas de estas son de su agrado. Se sabe que los nombres de las materias irán sin acentos y en minúsculas cuando sean recibidos por parámetro en la función.
Su solución debe tener una función de acuerdo con la siguiente especificación:
Nombre de la función: conteo_de_materias
Si lo requiere, puede agregar funciones adicionales.
Retorna el número de materias que cumplen los criterios para gustarle a Pedro.
<<<<<<<"""
def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str)->int :
    contador = 0

    if ("programacion" in nombre_materia_1 or
        "matematica" in nombre_materia_1 or
        "filosofia" in nombre_materia_1 or
        "literatura" in nombre_materia_1):
        contador += 1

    if ("programacion" in nombre_materia_2 or
        "matematica" in nombre_materia_2 or
        "filosofia" in nombre_materia_2 or
        "literatura" in nombre_materia_2):
        contador += 1

    if ("programacion" in nombre_materia_3 or
        "matematica" in nombre_materia_3 or
        "filosofia" in nombre_materia_3 or
        "literatura" in nombre_materia_3):
        contador += 1

    return contador