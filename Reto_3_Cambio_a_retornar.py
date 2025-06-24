# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:35:59 2025

@author: gabri
"""

def grados_a_radianes(grados: float) -> float:
    pi= 3.1416
    rad = (2*pi*grados)/360
    return rad

def invertir_numero(numero: int) -> int:
    unidades = numero % 10
    numero //=10
    decenas = numero % 10
    numero//= 10
    centenas= numero % 10
    numero //=10
    millares =numero % 10
    
    inverso= (unidades*1000)+(decenas*100)+(centenas*10)+millares
    return inverso

def calcular_cambio(cambio: int) -> str:
    a = cambio //500
    cambio = cambio%500
    b = cambio// 200
    cambio=cambio % 200
    c= cambio // 100
    cambio =cambio % 100
    d =cambio // 50
    
    inverso= str(a)+"A,"+str(b)+"B,"+str(c)+"C,"+str(d)+"D"
    return inverso