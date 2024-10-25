

producto = ""
lista_producto = []

while producto.lower() != "salir":
    producto = input("Ingrese el nombre del producto o salir: ")

    if producto.lower() != "salir":
        precio = float(input("Ingrese el precio: "))
        stock = input("Ingrese el stock: ")
        dicc_producto = { "nombre":producto, "precio":precio , "stock":stock }
        lista_producto.append(dicc_producto)


print("<------ LISTA DE PRODUCTO ------------>")
contador = 0
while contador < len(lista_producto):
    print("<-- PRODUCTO -->")
    print(f"Nombre: {lista_producto[contador]['nombre']}")
    print(f"Precio: {lista_producto[contador]['precio']}")
    print(f"Stock: {lista_producto[contador]['stock']}")
    print("")
    contador = contador + 1


