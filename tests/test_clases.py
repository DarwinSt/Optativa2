import pytest
from clases import Carrito, Inventario, CalculadoraDescuentos, Usuario, Tarea, Reserva

def test_carrito():
    carrito = Carrito()
    carrito.agregar_producto("manzana", 1.5)
    carrito.agregar_producto("pera", 2.0)
    assert carrito.subtotal == 3.5
    assert carrito.calcular_total() == 3.5
    assert carrito.calcular_total(10) == 3.15

def test_inventario():
    inventario = Inventario()
    inventario.agregar_producto(1, "Laptop", 5)
    assert inventario.consultar_producto(1) == {"nombre": "Laptop", "cantidad": 5}

def test_calculadora_descuentos():
    assert CalculadoraDescuentos.calcular_descuento(100, 20) == 80
    with pytest.raises(ValueError):
        CalculadoraDescuentos.calcular_descuento(-100, 20)

def test_usuario():
    usuario = Usuario()
    usuario.registrar_usuario("cristian", "cristian@example.com")
    assert usuario.iniciar_sesion("cristian") == True

def test_tarea():
    tarea = Tarea()
    tarea.crear_tarea(1, "Estudiar", "2024-12-01")
    assert len(tarea.listar_pendientes()) == 1

def test_reserva():
    reserva = Reserva()
    reserva.crear_reserva("2024-12-25", "18:00", 4)
    assert len(reserva.listar_reservas()) == 1
    assert reserva.verificar_disponibilidad("2024-12-25", "19:00") == True
