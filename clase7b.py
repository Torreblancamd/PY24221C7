#TUPLAS

alumnos_tupla = ("Jose","Mauro","Romina")

print(alumnos_tupla)

#ACCESO

print( alumnos_tupla[0])
print( alumnos_tupla[2])


#CUIDADO
#alumnos_tupla[0] = "Juan"




#Update

alumnos_lista  = list( alumnos_tupla )
alumnos_lista[0] = "Juan"

print(alumnos_tupla)
print(alumnos_lista)


alumnos_tupla = tuple(alumnos_lista)
print(alumnos_tupla)
print(alumnos_lista)


#LARGO

print( len(alumnos_lista) )






#SET

alumnos_set = {"Marcos","Ana","Ramon","Marcos"}

#NO ORDENADA

print(alumnos_set)

#print(alumnos_set[0]) OJO


cantidad = len(alumnos_set)
contador = 0

"""
while contador <= cantidad:
    print( alumnos_set[contador])
    contador = contador + 1 
"""


# DICCIONARIOS 
#LLAVE: NUMERICO, STRING
#VALOR: CUALQUIER TIPO DE DATO

usuarios = { "u1":"Pepe", "u2":"Marta","u3":"Juan"}

print(usuarios)

#ACCESO
print(usuarios["u2"])



#LISTA DE DICCIONARIOS

alumnos = [ {"nombre":"Pedro", "edad":30 , "materias":["Lengua","Fisica","Programacion"]} ,
            {"nombre":"Laura", "edad":19 , "materias":["Lengua","Ingles","Programacion"]},
            {"nombre":"Nicolas", "edad":26 , "materias":["Lengua","Fisica","Programacion"]}]


print(alumnos)
print(alumnos[1]["nombre"])
print(alumnos[1]["materias"])