def reverter_numero(num):
    num_rev = num[-1::-1]
    return num_rev


numero = input("Digite um numero: ")
numero_reverso = reverter_numero(numero)
print("O número reverso é: ", numero_reverso) 