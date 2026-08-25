# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 09:27:52 2025

@author: gabri
"""

def clasificar_regalo(id : int) -> str:
    if es_palindromo(id) :
        if is_odd(id):
            respuesta = "boy"
        else:
            respuesta="girl"
    else:
        if is_odd(id):
            respuesta="man"
        else:
            respuesta="woman"
    
    return respuesta
def es_palindromo(id: int) -> bool:
    id_tmp= str(id)
    return id_tmp == id_tmp[::-1]
        
def is_odd(number: int) -> bool:
    """Return True when the number is odd."""
    return number % 2 != 0