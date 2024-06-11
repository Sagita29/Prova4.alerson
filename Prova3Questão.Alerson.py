def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado
 
a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
print("O resultado de", a, "elevado a", b, "é:", potencia(a, b))



