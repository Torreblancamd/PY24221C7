

#LISTA 

nombres_alumnos = []
#nombre_alumnos = list()

colores = ["Rojo","Azul","Amarillo","Verde"]

print(colores)

#ORDENADAS---->INDEX
#ACCESO
print( colores[0])
print( colores[2])

#OJO
#colores = "Verde"
#print(colores)


#
lista_random = [ 10 , 20 , "Pedro", "Laura" , True , ["Raton","Gato"], 8.5]

print(lista_random)
print(lista_random[4])
print(lista_random[6])
print(lista_random[5][1])

#resultado = lista_random[5]
#print(resultado[1])


#MUTABLES

lista_random[0] = 9 

print(lista_random)


#METODOS

nombres_alumnos = ["Juan","Laura"]
print(nombres_alumnos)

#APPEND
nombres_alumnos.append("Mateo")

print("APPEND: ",nombres_alumnos)


#INSERT

nombres_alumnos.insert(1, "Marta")
print("INSERT: ",nombres_alumnos)


#POP SIN INDEX

nombres_alumnos.pop()
print("POP: ",nombres_alumnos)


#POP CON INDEX

eliminado = nombres_alumnos.pop(1)
print("POP: ",nombres_alumnos)
print(f"Se elimino a: {eliminado} ")


#REMOVE
nombres_alumnos.remove("Laura")
print("REMOVE: ",nombres_alumnos)

#OJO
#nombres_alumnos.remove("Laura")
#print("REMOVE: ",nombres_alumnos)

#INDEX
print( nombres_alumnos.index("Juan"))
#print( nombres_alumnos.index("Laura"))