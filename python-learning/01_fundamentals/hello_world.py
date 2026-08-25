# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:22:05 2025

@author: gabri
"""

def saludar(nombre: str)-> str:
   return "Hola " + nombre + "!"

nombre = input("¿Cuál es su nombre? ")
saludo = saludar(nombre)
print(saludo)