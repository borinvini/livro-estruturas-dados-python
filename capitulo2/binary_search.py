def busca_binaria(dados, valor_procurado):
    """
    Realiza busca binária em uma lista ordenada.
    Retorna a posição (base-1) se encontrado, ou -1 caso contrário.
    """
    inicio = 0
    fim = len(dados) - 1
    achou = 0
    posicao = -1
    
    while (inicio <= fim) and (achou == 0):
        meio = (inicio + fim) // 2
        
        if dados[meio] == valor_procurado:
            achou = 1
            posicao = meio
        elif dados[meio] < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    if achou == 0:
        return -1
    else:
        return posicao + 1

def main():
        
    import random
    # Gerando 10 valores únicos dentro de um intervalo de 0 até 9
    dados = random.sample(range(10), 10)
    print("Array original:", dados)
    
    # IMPORTANTE: Busca binária requer dados ordenados!
    dados.sort()
    print("Array ordenado:", dados)
    
    valor_procurado = int(input('Digite o valor que deseja buscar: '))
    
    achou = busca_binaria(dados, valor_procurado)
    
    if achou == -1:
        print('Valor não encontrado.')
    else:
        print(f'Valor encontrado no índice {achou}')

if __name__ == "__main__":
    main()