def busca_sequencial(dados, valor_procurado):
    achou = 0
    i = 0
    while (((i < len(dados))) and (achou == 0)):
        if (dados[i] == valor_procurado):
            achou = 1
        else:
            i+=1
    
    if (achou == 0):
        return -1
    else:
        return i

def main():
    """
    Gera uma lista aleatória e permite ao usuário buscar um valor.
    """
    import random
    # Gerando 10 valores únicos dentro de um intervalo de 0 até 9
    dados = random.sample(range(10), 10)
    print("Array gerado:", dados)
    
    valor_procurado = int(input('Digite o valor para buscar: '))
    
    achou = busca_sequencial(dados, valor_procurado)
    
    if (achou == -1):
        print('Valor não encontrado.')
    else:
        print(f'Valor encontrado no índice {achou}')

if __name__ == "__main__":
    main()