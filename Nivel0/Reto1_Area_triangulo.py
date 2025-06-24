# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:34:56 2025

@author: gabri
"""
import math
s1 = float(input("Ingrese un lado: "))
s2 = float(input("Ingrese otro lado: "))
s3 = float(input("Ingrese otro lado: "))

def area_triangulo(s1: float, s2: float, s3: float) -> float:
    #calcular subperimetro
    s= float((s1+s2+s3)/2)
    area=math.sqrt((s*(s-s1)*(s-s2)*(s-s3)))
    
    return round(area,1)

print("El área del triángulo es de: "+ str(area_triangulo(s1, s2, s3)))