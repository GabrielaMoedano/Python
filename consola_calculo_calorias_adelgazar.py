# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 16:13:36 2025

@author: gabri
"""

import calculadora_indices as calc
def iniciar_aplicacion() ->None:
    print(" Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar")

    peso = float(input("Ingrese Peso de la persona en kilogramos: "))
    altura = float(input("Ingrese Altura de la persona en metros: "))
    edad = int(input("Ingrese Edad de la persona en años: "))
    valor_genero = int(input("Valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161: "))
   
    print( str(calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)))
        
  
    
iniciar_aplicacion()