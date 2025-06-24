# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:38:05 2025

@author: gabri
"""

def calcular_horario_llegada(hora_salida:int, minuto_salida:int,segundo_salida: int,
    duracion_horas: int,duracion_minutos:int,duracion_segundos:int)-> str:
#Valida entradas   
    if(hora_salida <24) and (minuto_salida<60) and (segundo_salida<60):
        
        #suma segundos
        if( segundo_salida+duracion_segundos)>60 :
            segundos =(segundo_salida+duracion_segundos)%60

        else:    
            segundos =(segundo_salida+duracion_segundos)
        
        
        #suma minutos
        #print(residuo_seg)
        if (minuto_salida+duracion_minutos +((segundo_salida+duracion_segundos)//60))>60:
            minutos=(minuto_salida+duracion_minutos +(segundo_salida+duracion_segundos)//60)%60
           
        else:
            minutos=(minuto_salida+duracion_minutos +((segundo_salida+duracion_segundos)//60))
       
            
        #suma horas
        if (hora_salida+duracion_horas+((minuto_salida+duracion_minutos +((segundo_salida+duracion_segundos)//60))//60))>23 :  
            
            hora=(hora_salida+duracion_horas+((minuto_salida+duracion_minutos +((segundo_salida+duracion_segundos)//60))//60))%24
        else:
            hora=(hora_salida+duracion_horas+((minuto_salida+duracion_minutos +((segundo_salida+duracion_segundos)//60))//60))
        
        return str(hora)+":"+str(minutos)+":"+str(segundos)
    else :
        print("Error en la hora ingresada")