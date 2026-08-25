# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 11:48:46 2025

@author: gabri
"""

def es_divisible(n: int, d: int) -> int:
    if d==0:
        respuesta = 0
        
    elif n%(2*d)  ==0 :
        respuesta = 2
        
    elif n%d ==0 :
        respuesta = 1
    
    else:
        respuesta = 0
        
    return respuesta