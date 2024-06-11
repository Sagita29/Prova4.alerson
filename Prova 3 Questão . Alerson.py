def potencia(a,b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    else:
        for _ in range(-b):
            resultado *= a
        resultado = 1 /resultado
    return resultado

print(potencia(2, -3))



