# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 15:47:52 2025

@author: gabri

consola_calculo_calorias_reposo.py
"""

import calculadora_indices as calc
def iniciar_aplicacion() ->None:
    print(" Calcula la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal)")
    peso = float(input("Ingrese Peso de la persona en kilogramos: "))
    altura = float(input("Ingrese Altura de la persona en metros: "))
    edad = int(input("Ingrese Edad de la persona en años: "))
    valor_genero = int(input("Valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161: "))
    
    tmb = float(calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero))
    
    print("La cantidad de calorías que la persona quema en reposo es: "+ str(tmb))
    
iniciar_aplicacion()