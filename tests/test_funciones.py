import pytest
from funciones import es_numero_par, obtener_edad, generar_identificador, ordenar_por_tamano

def test_es_numero_par():
    assert es_numero_par(8) is True
    assert es_numero_par(3) is False
    assert es_numero_par(0) is True
    assert es_numero_par(-6) is True

def test_obtener_edad():
    assert obtener_edad("2000-05-15") == 24
    assert obtener_edad("2024-12-31") == 0

def test_generar_identificador():
    id1 = generar_identificador()
    id2 = generar_identificador()
    assert len(id1) == 8
    assert id1.isalnum()
    assert id1 != id2

def test_ordenar_por_tamano():
    assert ordenar_por_tamano(["casa", "arbol", "automovil"]) == ["casa", "arbol", "automovil"]
    assert ordenar_por_tamano([]) == []
