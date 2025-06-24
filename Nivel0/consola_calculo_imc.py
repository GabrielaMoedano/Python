# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 15:11:29 2025

@author: gabri
"""

"""consola_calculo_imc.py"""
import calculadora_indices as calc


def consola_calculo_imc()->None:
    print("Calcula el índice de masa corporal de una persona a partir de la ecuación definida ")

    peso = float(input("Ingrese Peso de la persona en kilogramos: "))
    altura = float(input("Altura de la persona en metros :"))
    
    imc = calc.calcular_IMC(peso,altura)
    print("El valor del IMC es "+ str(imc))
    
consola_calculo_imc()