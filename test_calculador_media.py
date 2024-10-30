import pytest
from calculador_media import calcula_media

def test_calcula_media_basico():
    """Teste básico com valores comuns para calcular a média."""
    assert calcula_media(7, 8, 9) == 8.0

def test_todas_notas_zero():
    """Teste onde todas as notas são zero."""
    assert calcula_media(0, 0, 0) == 0.0

def test_notas_maximas():
    """Teste onde todas as notas têm valores máximos possíveis."""
    assert calcula_media(10, 10, 10) == 10.0

def test_notas_decimais():
    """Teste onde as notas possuem valores decimais."""
    assert calcula_media(7.5, 8.5, 9.5) == 8.5

def test_mistura_valores():
    """Teste onde há uma mistura de notas com zero e valores máximos."""
    assert calcula_media(0, 10, 5) == 5.0
