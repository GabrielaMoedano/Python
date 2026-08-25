# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:59:04 2026

@author: gabri
"""

def buscar_estudiante(est1: dict,est2: dict,est3: dict,est4: dict,nom: str)-> dict:
    buscado = None
    if est1['nombre'] == nom:
        buscado = est1
    elif est2['nombre'] == nom:
        buscado = est2
    elif est3['nombre'] == nom:
        buscado = est3
    elif est4['nombre'] == nom:
        buscado = est4
    return buscado        

def avanzar_semestre(est1: dict,est2: dict,est3: dict,est4: dict)-> None:
    est1["ssc"] +=1
    est2["ssc"] +=1
    est3["ssc"] +=1
    est4["ssc"] +=1
    
    
def quienes_en_riesgo(est1: dict,est2: dict,est3: dict,est4: dict)-> dict:
    en_riesgo = {}
    if est1["promedio"] < 3.4:
        en_riesgo[est1["codigo"]] =est1["promedio"]
    if est2["promedio"] < 3.4:
        en_riesgo[est2["codigo"]] =est2["promedio"]
    if est3["promedio"] < 3.4:
        en_riesgo[est3["codigo"]] =est3["promedio"]
    if est4["promedio"] < 3.4:
        en_riesgo[est4["codigo"]] =est4["promedio"]
        
    return en_riesgo

def mejor_del_salon(estudiante1: dict, estudiante2: dict, estudiante3: dict,
                    estudiante4: dict, estudiante5: dict) -> str:

    mejor = estudiante1

   # promedio_e1 = calcular_promedio(estudiante1)
    promedio_e2 = calcular_promedio(estudiante2)
    promedio_e3 = calcular_promedio(estudiante3)
    promedio_e4 = calcular_promedio(estudiante4)
    promedio_e5 = calcular_promedio(estudiante5)

    if promedio_e2 > calcular_promedio(mejor):
        mejor = estudiante2
    elif promedio_e2 == calcular_promedio(mejor):
        if estudiante2["nombre"].lower() < mejor["nombre"].lower():
            mejor = estudiante2

    if promedio_e3 > calcular_promedio(mejor):
        mejor = estudiante3
    elif promedio_e3 == calcular_promedio(mejor):
        if estudiante3["nombre"].lower() < mejor["nombre"].lower():
            mejor = estudiante3

    if promedio_e4 > calcular_promedio(mejor):
        mejor = estudiante4
    elif promedio_e4 == calcular_promedio(mejor):
        if estudiante4["nombre"].lower() < mejor["nombre"].lower():
            mejor = estudiante4

    if promedio_e5 > calcular_promedio(mejor):
        mejor = estudiante5
    elif promedio_e5 == calcular_promedio(mejor):
        if estudiante5["nombre"].lower() < mejor["nombre"].lower():
            mejor = estudiante5

    return mejor["nombre"]

def calcular_promedio(est: dict) -> float:
    promedio = (
        est["matematicas"] +
        est["español"] +
        est["ciencias"] +
        est["literatura"] +
        est["arte"]
    ) / 5
    
    return promedio
##PROGRAMA PRINCIPAL
"""
e_1 ={"nombre":"Lina","matematicas":4,"español":4.3,"ciencias":4.7,"literatura":4.78,"arte":4}
e_2 ={"nombre":"Carlos","matematicas":2.4,"español":3.3,"ciencias":3.7,"literatura":4.78,"arte":4}
e_3 ={"nombre":"Alberto","matematicas":3.4,"español":4.3,"ciencias":3.7,"literatura":4.78,"arte":4}
e_4 ={"nombre":"Gabriela","matematicas":4.5,"español":4.3,"ciencias":4.7,"literatura":4.78,"arte":4}
e_5 ={"nombre":"Alexis","matematicas":5,"español":3,"ciencias":2,"literatura":4.78,"arte":4}
"""
estudiante1 = {'nombre': 'pablo', 'matematicas': 3.4, 'español': 5.0, 'ciencias': 2.9, 'literatura': 4.2, 'arte': 3.2}
estudiante2 = {'nombre': 'andres', 'matematicas': 2.1, 'español': 5.0, 'ciencias': 3.0, 'literatura': 4.1, 'arte': 3.5}
estudiante3 = {'nombre': 'daniela', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}
estudiante4 = {'nombre': 'maria', 'matematicas': 3.2, 'español': 3.7, 'ciencias': 3.1, 'literatura': 4.7, 'arte': 3.4}
estudiante5 = {'nombre': 'pedro', 'matematicas': 4.7, 'español': 4.2, 'ciencias': 4.3, 'literatura': 2.5, 'arte': 4.2}

mejor = mejor_del_salon(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5)

print(mejor)

"""    

e_1 ={"nombre":"Lina","codigo":"20202101234","genero":"femenino","carrera":"sistemas","promedio":4.78,"ssc":4}
e_2 ={"nombre":"Laura","codigo":"20202105678","genero":"femenino","carrera":"Civil","promedio":3.21,"ssc":1}
e_3 ={"nombre":"Felipe","codigo":"20202109012","genero":"masculino","carrera":"sistemas","promedio":2.9,"ssc":2}
e_4 ={"nombre":"Carlos","codigo":"20202103456","genero":"masculino","carrera":"Economia","promedio":3.89,"ssc":3}

nombre =input("Ingrese el nombre del estudiante a buscar:")

est_buscado= buscar_estudiante(e_1, e_2, e_3, e_4, nombre)

if est_buscado is None:
    print("El estudiante no existe")
else:
    print("El estudiante existe y su codigo es:"+est_buscado["codigo"])
    """
###Para funcion2
"""
print("Semestre estufiante 1:", e_1["ssc"])
print("Semestre estufiante 2:", e_2["ssc"])
print("Semestre estufiante 3:", e_3["ssc"])
print("Semestre estufiante 4:", e_4["ssc"])   

avanzar_semestre(e_1, e_2, e_3, e_4) 
print("Semestre nuevo estufiante 1:", e_1["ssc"])
print("Semestre nuevo estufiante 2:", e_2["ssc"])
print("Semestre nuevo estufiante 3:", e_3["ssc"])
print("Semestre nuevo estufiante 4:", e_4["ssc"]) 
"""

"""
###Para funcion 3
riesgo = quienes_en_riesgo(e_1, e_2, e_3, e_4)
                           
print(riesgo)  

"""                  