# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 15:37:05 2025

@author: gabri
"""

"""consola_calculo_porcentaje_grasa.py"""
import calculadora_indices as calc
def iniciar_aplicacion() ->None:
    print("Calcula el porcentaje de grasa de una persona a partir de la ecuación definida anteriormente")
    peso = float(input("Ingrese Peso de la persona en kilogramos: "))
    altura = float(input("Ingrese Altura de la persona en metros: "))
    edad = int(input("Ingrese Edad de la persona en años: "))
    valor_genero = float(input("Ingrese Valor que varía según el género de la persona: en caso de ser masculino debe ser 10.8 y en caso de ser femenino debe ser 0: "))
    
    gc = float(calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero))
    
    print("El % de grasa es: "+ str(gc))
    
iniciar_aplicacion()