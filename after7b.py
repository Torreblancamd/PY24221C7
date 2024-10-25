


lista_producto = [{"nombre":"Lampara", "precio":5000 ,"stock":5},
                  {"nombre":"Radio", "precio":12000 ,"stock":7},
                  {"nombre":"Mouse", "precio":8400 ,"stock":3},
                  {"nombre":"Teclado", "precio":15200 ,"stock":9},
                  {"nombre":"Microfono", "precio":19000 ,"stock":5},
                  {"nombre":"Camara", "precio":9300 ,"stock":2},
                  ]



producto = input("Ingrese el nombre del producto que quiere buscar")
contador = 0
while contador < len(lista_producto):

    if lista_producto[contador]["nombre"] == producto:
        print("<-- PRODUCTO -->")
        print(f"Nombre: {lista_producto[contador]['nombre']}")
        print(f"Precio: {lista_producto[contador]['precio']}")
        print(f"Stock: {lista_producto[contador]['stock']}")
        print("")
        break
    
    
    contador = contador + 1
    if contador == len(lista_producto):
        print(f"No encontramos el producto: {producto}")