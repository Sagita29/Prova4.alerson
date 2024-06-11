def maior(*args):
    if len(args) == 0:
        return None
    maior_valor = args[0]
    for valor in args[1:]:
        if valor > maior_valor:
            maior_valor = valor
    return maior_valor
 
def main():
    valores = []
    n = int(input("Quantos números você quer comparar? "))
    for i in range(n):
        valor = int(input("Digite o número {}: ".format(i + 1)))
        valores.append(valor)
    print("O maior valor é:", maior(*valores))
 
if __name__ == "__main__":
    main()