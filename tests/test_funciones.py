import pytest
from funciones import es_par, calcular_edad, generar_id, ordenar_por_longitud

def test_es_par():
    assert es_par(4) == True
    assert es_par(7) == False
    assert es_par(0) == True
    assert es_par(-2) == True

def test_calcular_edad():
    assert calcular_edad("2000-01-01") == 24
    assert calcular_edad("2024-01-01") == 0

def test_generar_id():
    id1 = generar_id()
    id2 = generar_id()
    assert len(id1) == 8
    assert id1.isalnum()
    assert id1 != id2

def test_ordenar_por_longitud():
    assert ordenar_por_longitud(["perro", "gato", "elefante"]) == ["gato", "perro", "elefante"]
    assert ordenar_por_longitud([]) == []
