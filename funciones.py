import random
import string
from datetime import datetime

def generar_identificador():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.sample(caracteres, 8))

def es_numero_par(numero):
    return numero % 2 == 0

def obtener_edad(fecha_nac):
    fecha_nacimiento = datetime.strptime(fecha_nac, "%Y-%m-%d")
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

def ordenar_por_tamano(palabras):
    return sorted(palabras, key=lambda palabra: len(palabra))
