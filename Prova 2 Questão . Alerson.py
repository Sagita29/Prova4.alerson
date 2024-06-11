def contar_digitos(numero):
    if numero == 0:  
        return 1
    contador = 0
    while numero != 0:
        contador += 1
        numero //= 10
    return contador
 
# Exemplo de uso
numero = 62345
print("O número", numero, "tem", contar_digitos(numero), "dígitos.")