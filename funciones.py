import random
import string

def generar_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def es_par(n):
    return n % 2 == 0

def calcular_edad(fecha_nacimiento):
    from datetime import datetime
    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.now()
    return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))


def ordenar_por_longitud(lista_palabras):
    return sorted(lista_palabras, key=len)
