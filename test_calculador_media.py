import pytest
from calculador_media import calcula_media

def test_calcula_media_basico():
    """Teste básico com valores comuns para calcular a média."""
    assert calcula_media(7, 8, 9) == 8.0, "Erro: A média de 7, 8 e 9 deve ser 8.0"

def test_todas_notas_zero():
    """Teste onde todas as notas são zero."""
    assert calcula_media(0, 0, 0) == 0.0, "Erro: A média de 0, 0 e 0 deve ser 0.0"

def test_notas_maximas():
    """Teste onde todas as notas têm valores máximos possíveis."""
    assert calcula_media(10, 10, 10) == 10.0, "Erro: A média de 10, 10 e 10 deve ser 10.0"

def test_notas_decimais():
    """Teste onde as notas possuem valores decimais."""
    assert calcula_media(7.5, 8.5, 9.5) == 8.5, "Erro: A média de 7.5, 8.5 e 9.5 deve ser 8.5"

def test_mistura_valores():
    """Teste onde há uma mistura de notas com zero e valores máximos."""
    assert calcula_media(0, 10, 5) == 5.0, "Erro: A média de 0, 10 e 5 deve ser 5.0"

def test_tipo_invalido():
    """Teste para verificar se a função lança TypeError para entradas inválidas."""
    with pytest.raises(TypeError, match="Todas as notas devem ser números"):
        calcula_media("10", 8, 9)  # Passando uma string para simular erro de tipoD
