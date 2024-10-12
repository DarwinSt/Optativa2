from funciones import es_par, calcular_edad, generar_id, ordenar_por_longitud
from clases import Carrito

if __name__ == "__main__":
    print("Es 4 par?:", es_par(4))
    print("Edad de alguien nacido en 2000-01-01:", calcular_edad("2000-01-01"))
    print("Generar un ID único:", generar_id())
    print("Ordenar palabras por longitud:", ordenar_por_longitud(["sol", "estrella", "luna"]))

    carrito = Carrito()
    carrito.agregar_producto("manzana", 1.5)
    carrito.agregar_producto("pera", 2.0)
    print("Subtotal del carrito:", carrito.subtotal)
