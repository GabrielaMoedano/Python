# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:18:44 2025

@author: gabri
"""
pesos = float(input("Ingrese la cantidad dinero: "))
intereses = float(input("Ingrese la tasa de interes: "))
anios = int(input("Ingrese el numero de años: "))

resultado = pesos * (1+intereses/100)**anios


print("El valor futuro es de $"+str(round(resultado,3))+" con un plazo de "+ str(anios)+" años con una tasa de interes de "+str(intereses)+"% de valor anual")
      