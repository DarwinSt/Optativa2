from funciones import es_numero_par, obtener_edad, generar_identificador, ordenar_por_tamano
from clases import CestaCompra

if __name__ == "__main__":
    print("¿Es 4 un número par?:", es_numero_par(4))
    print("Edad de una persona nacida en 2000-01-01:", obtener_edad("2000-01-01"))
    print("Generar un identificador único:", generar_identificador())
    print("Ordenar palabras por tamaño:", ordenar_por_tamano(["sol", "estrella", "luna"]))

    cesta = CestaCompra()
    cesta.anadir_item("manzana", 1.5)
    cesta.anadir_item("pera", 2.0)
    print("Subtotal de la cesta de compra:", cesta.precio_bruto)