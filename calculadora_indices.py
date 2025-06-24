# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:59:46 2025

@author: gabri
"""

def calcular_IMC(peso: float, altura: float) -> float:
    imc = peso/(altura**2)
    return round(imc,2)
   
def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    imc = calcular_IMC(peso, altura)
    gc= 1.2 * imc +0.23*edad -5.4 -valor_genero
    return round(gc,2)
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    tmb = 10*peso + (6.25 * altura*100) -(5*edad) + valor_genero
    return round(tmb)
def calcular_calorias_en_actividad (peso: float, altura: float, edad: int, valor_genero: int,valor_actividad: float) -> float:
    tmb_actividad_fisica = calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad
    return round(tmb_actividad_fisica,2)
def consumo_calorias_recomendado_para_adelgazar(peso : float, altura: float, edad: int, valor_genero: int) -> str:
    xxx = round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.80,2)
    zzz = round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.85,2)
    
    return print("Para adelgazar es recomendado que consumas entre: "+ str(xxx) +" y "+ str(zzz) +" calorías al día.")
    