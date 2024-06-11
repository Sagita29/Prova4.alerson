def contar_digitos(numero):
    if numero == 0:  
        return 1
    contador = 0
    while numero != 0:
        contador += 1
        numero //= 10
    return contador
 
numero = int(input("Digite um número inteiro: "))
print("O número", numero, "tem", contar_digitos(numero), "dígitos.")