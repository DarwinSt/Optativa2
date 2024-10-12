# clases.py

class Carrito:
    def __init__(self):
        self.productos = {}
        self.subtotal = 0

    def agregar_producto(self, nombre, precio):
        if nombre in self.productos:
            self.productos[nombre]['cantidad'] += 1
        else:
            self.productos[nombre] = {'precio': precio, 'cantidad': 1}
        self.subtotal += precio

    def calcular_total(self, descuento=0):
        total = self.subtotal * (1 - descuento / 100)
        return total if total > 0 else 0


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto, nombre, cantidad):
        if id_producto in self.productos:
            raise ValueError("ID de producto ya existe.")
        self.productos[id_producto] = {'nombre': nombre, 'cantidad': cantidad}

    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            raise ValueError("ID de producto no existe.")
        del self.productos[id_producto]

    def actualizar_stock(self, id_producto, cantidad):
        if id_producto not in self.productos:
            raise ValueError("ID de producto no existe.")
        self.productos[id_producto]['cantidad'] = cantidad

    def consultar_producto(self, id_producto):
        if id_producto not in self.productos:
            raise ValueError("ID de producto no existe.")
        return self.productos[id_producto]


class CalculadoraDescuentos:
    @staticmethod
    def calcular_descuento(precio, porcentaje):
        if precio < 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        return precio * (1 - porcentaje / 100)


class Usuario:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre, email):
        if nombre in self.usuarios:
            raise ValueError("Nombre de usuario ya registrado.")
        self.usuarios[nombre] = email

    def iniciar_sesion(self, nombre):
        if nombre not in self.usuarios:
            raise ValueError("Usuario no encontrado.")
        return True

    def recuperar_contrasena(self, email):
        if email not in self.usuarios.values():
            raise ValueError("Email no registrado.")
        return f"Enlace de recuperación enviado a {email}"


class Tarea:
    def __init__(self):
        self.tareas = {}

    def crear_tarea(self, id_tarea, titulo, fecha_vencimiento):
        if id_tarea in self.tareas:
            raise ValueError("ID de tarea ya existe.")
        self.tareas[id_tarea] = {'titulo': titulo, 'fecha_vencimiento': fecha_vencimiento, 'completada': False}

    def marcar_completada(self, id_tarea):
        if id_tarea not in self.tareas:
            raise ValueError("ID de tarea no encontrada.")
        self.tareas[id_tarea]['completada'] = True

    def eliminar_tarea(self, id_tarea):
        if id_tarea not in self.tareas:
            raise ValueError("ID de tarea no encontrada.")
        del self.tareas[id_tarea]

    def listar_pendientes(self):
        return [tarea for tarea in self.tareas.values() if not tarea['completada']]


class Reserva:
    def __init__(self):
        self.reservas = []

    def crear_reserva(self, fecha, hora, num_personas):
        self.reservas.append({'fecha': fecha, 'hora': hora, 'num_personas': num_personas})

    def cancelar_reserva(self, fecha, hora):
        self.reservas = [r for r in self.reservas if not (r['fecha'] == fecha and r['hora'] == hora)]

    def verificar_disponibilidad(self, fecha, hora):
        return all(r['fecha'] != fecha or r['hora'] != hora for r in self.reservas)

    def listar_reservas(self):
        return self.reservas
