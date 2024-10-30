def calcula_media(nota1, nota2, nota3):
    if not all(isinstance(nota, (int, float)) for nota in [nota1, nota2, nota3]):
        raise TypeError("Todas as notas devem ser números (int ou float).")
    return (nota1 + nota2 + nota3) / 3