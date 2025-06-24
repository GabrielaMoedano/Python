# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:23:33 2025

@author: gabri
"""

def calcular_BMI(peso_lb: float, altura_inch: float) -> float:
    peso = peso_lb*0.45
    altura = altura_inch *0.025
    bmi= peso/(altura**2)
    return round(bmi,2)

peso_lb = float(input("Ingrese su peso en libras:"))
altura_inch = float(input("Ingrese su altura en pulgadas: "))
print("El BMI es: "+str(calcular_BMI(peso_lb, altura_inch)))