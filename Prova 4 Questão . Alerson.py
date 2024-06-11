def maior(*args):
    if len(args) == 0:
        return None
    maior_valor = args[0]
    for valor in args[1:]:
        if valor > maior_valor:
            maior_valor = valor
    return maior_valor
 
# Exemplo de uso
def main():
    valores = [80, 57, 2, 189, 89]
    print("O maior valor é:", maior(*valores))
 
if __name__ == "__main__":
    main()