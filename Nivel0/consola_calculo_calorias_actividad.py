# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 16:02:42 2025

@author: gabri
consola_calculo_calorias_actividad.py
"""


import calculadora_indices as calc
def iniciar_aplicacion() ->None:
    print(" Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física (esto es, su tasa metabólica basal según actividad física)")
    print("Considera los valores para valor_actividad: "+
            " 1.2: poco o ningún ejercicio"+
            " 1.375: ejercicio ligero (1 a 3 días a la semana)"+
            " 1.55: ejercicio moderado (3 a 5 días a la semana)"+
            "1.72: deportista (6 -7 días a la semana)"+
            "1.9: atleta (entrenamientos mañana y tarde.")
    peso = float(input("Ingrese Peso de la persona en kilogramos: "))
    altura = float(input("Ingrese Altura de la persona en metros: "))
    edad = int(input("Ingrese Edad de la persona en años: "))
    valor_genero = int(input("Valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161: "))
    valor_actividad = float(input("Valor que depende de la actividad física semanal y toma los valores descriptos anteriormente: "))
    tmb = float(calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad))
    
    print("La cantidad de calorías que una persona quema, al realizar algún tipo de actividad física semanalmente es: "+ str(tmb))
    
iniciar_aplicacion()