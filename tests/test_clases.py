import pytest
from clases import CestaCompra, GestionInventario, GestorDescuentos, AdministracionUsuarios, GestionTareas, SistemaReservas

def test_cesta_compra():
    cesta = CestaCompra()
    cesta.anadir_item("manzana", 1.5)
    cesta.anadir_item("pera", 2.0)
    assert cesta.precio_bruto == 3.5
    assert cesta.obtener_total() == 3.5
    assert cesta.obtener_total(10) == 3.15

def test_gestion_inventario():
    inventario = GestionInventario()
    inventario.insertar_producto(1, "Laptop", 5)
    assert inventario.ver_producto(1) == {"nombre": "Laptop", "cantidad": 5}

def test_gestor_descuentos():
    assert GestorDescuentos.aplicar_descuento(100, 20) == 80
    with pytest.raises(ValueError):
        GestorDescuentos.aplicar_descuento(-100, 20)

def test_administracion_usuarios():
    usuarios = AdministracionUsuarios()
    usuarios.registrar("cristian", "cristian@example.com")
    assert usuarios.autenticar("cristian") is True

def test_gestion_tareas():
    tareas = GestionTareas()
    tareas.crear(1, "Estudiar", "2024-12-01")
    assert len(tareas.ver_pendientes()) == 1

def test_sistema_reservas():
    reservas = SistemaReservas()
    reservas.hacer_reserva("2024-12-25", "18:00", 4)
    assert len(reservas.ver_reservas()) == 1
    assert reservas.hay_disponibilidad("2024-12-25", "19:00") is True
