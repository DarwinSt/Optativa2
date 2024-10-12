# carrito_compras.py

class CestaCompra:
    def __init__(self):
        self.items = {}
        self.precio_bruto = 0

    def anadir_item(self, nombre, precio):
        if nombre in self.items:
            self.items[nombre]['cantidad'] += 1
        else:
            self.items[nombre] = {'precio': precio, 'cantidad': 1}
        self.precio_bruto += precio

    def obtener_total(self, rebaja=0):
        total = self.precio_bruto * (1 - rebaja / 100)
        return max(0, total)


class GestionInventario:
    def __init__(self):
        self.catalogo = {}

    def insertar_producto(self, id_producto, nombre, cantidad):
        if id_producto in self.catalogo:
            raise ValueError("El ID del producto ya está registrado.")
        self.catalogo[id_producto] = {'nombre': nombre, 'cantidad': cantidad}

    def quitar_producto(self, id_producto):
        if id_producto not in self.catalogo:
            raise ValueError("El ID del producto no existe.")
        del self.catalogo[id_producto]

    def modificar_stock(self, id_producto, cantidad):
        if id_producto not in self.catalogo:
            raise ValueError("El ID del producto no existe.")
        self.catalogo[id_producto]['cantidad'] = cantidad

    def ver_producto(self, id_producto):
        if id_producto not in self.catalogo:
            raise ValueError("El ID del producto no existe.")
        return self.catalogo[id_producto]


class GestorDescuentos:
    @staticmethod
    def aplicar_descuento(precio, porcentaje):
        if precio < 0:
            raise ValueError("El precio debe ser positivo.")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100.")
        return precio * (1 - porcentaje / 100)


class AdministracionUsuarios:
    def __init__(self):
        self.registro_usuarios = {}

    def registrar(self, nombre, correo):
        if nombre in self.registro_usuarios:
            raise ValueError("El nombre de usuario ya está registrado.")
        self.registro_usuarios[nombre] = correo

    def autenticar(self, nombre):
        if nombre not in self.registro_usuarios:
            raise ValueError("Usuario no encontrado.")
        return True

    def restablecer_clave(self, correo):
        if correo not in self.registro_usuarios.values():
            raise ValueError("Correo no registrado.")
        return f"Enlace de recuperación enviado a {correo}"


class GestionTareas:
    def __init__(self):
        self.lista_tareas = {}

    def crear(self, id_tarea, titulo, fecha_limite):
        if id_tarea in self.lista_tareas:
            raise ValueError("El ID de la tarea ya existe.")
        self.lista_tareas[id_tarea] = {'titulo': titulo, 'fecha_limite': fecha_limite, 'finalizada': False}

    def marcar_como_finalizada(self, id_tarea):
        if id_tarea not in self.lista_tareas:
            raise ValueError("El ID de la tarea no fue encontrado.")
        self.lista_tareas[id_tarea]['finalizada'] = True

    def borrar_tarea(self, id_tarea):
        if id_tarea not in self.lista_tareas:
            raise ValueError("El ID de la tarea no fue encontrado.")
        del self.lista_tareas[id_tarea]

    def ver_pendientes(self):
        return [tarea for tarea in self.lista_tareas.values() if not tarea['finalizada']]


class SistemaReservas:
    def __init__(self):
        self.lista_reservas = []

    def hacer_reserva(self, fecha, hora, personas):
        self.lista_reservas.append({'fecha': fecha, 'hora': hora, 'personas': personas})

    def anular_reserva(self, fecha, hora):
        self.lista_reservas = [reserva for reserva in self.lista_reservas if not (reserva['fecha'] == fecha and reserva['hora'] == hora)]

    def hay_disponibilidad(self, fecha, hora):
        return all(reserva['fecha'] != fecha or reserva['hora'] != hora for reserva in self.lista_reservas)

    def ver_reservas(self):
        return self.lista_reservas
