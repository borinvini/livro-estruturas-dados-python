def quickSort(dados, inicio, fim):
    """
    Implementa o algoritmo Quick Sort usando divisão e conquista.
    
    Parâmetros:
        dados: lista a ser ordenada
        inicio: índice inicial do segmento a ordenar
        fim: índice final do segmento a ordenar
    """
    # Condição de parada: só ordena se houver pelo menos 2 elementos
    if inicio < fim:
        # Particiona a lista e obtém a posição final do pivô
        indice_pivo = particionar(dados, inicio, fim)
        
        # Ordena recursivamente a parte esquerda (menores que o pivô)
        quickSort(dados, inicio, indice_pivo - 1)
        
        # Ordena recursivamente a parte direita (maiores que o pivô)
        quickSort(dados, indice_pivo + 1, fim)


def particionar(dados, inicio, fim):
    """
    Particiona a lista em 2: elementos menores e maiores que o pivô.
    
    Retorna:
        A posição final do pivô na lista particionada
    """
    # Escolhe o primeiro elemento como pivô
    pivo = dados[inicio]
    
    # Percorre da esq p/ dir buscando elementos maiores que o pivô
    indice_esquerda = inicio + 1
    
    # Percorre da dir p/ esq buscando elementos menores que o pivô
    indice_direita = fim
    
    # Flag que indica quando os índices se cruzaram
    indices_cruzaram = False
    
    # Loop principal: continua até os índices se cruzarem
    while not indices_cruzaram:
        # Move índice esquerdo até encontrar elemento maior que o pivô
        while (indice_esquerda <= indice_direita 
               and dados[indice_esquerda] <= pivo):
            indice_esquerda += 1
        
        # Move índice direito até encontrar elemento menor que o pivô
        while (dados[indice_direita] >= pivo 
               and indice_direita >= indice_esquerda):
            indice_direita -= 1
        
        # Verifica se os índices se cruzaram
        if indice_direita < indice_esquerda:
            indices_cruzaram = True
        else:
            # Troca os elementos que estão fora de ordem
            aux = dados[indice_esquerda]
            dados[indice_esquerda] = dados[indice_direita]
            dados[indice_direita] = aux
    
    # Coloca o pivô em sua posição final (entre menores e maiores)
    auxiliar = dados[inicio]
    dados[inicio] = dados[indice_direita]
    dados[indice_direita] = auxiliar
    
    # Retorna a posição final do pivô
    return indice_direita


def main():
    """
    Função principal que demonstra o uso do Quick Sort.
    """
    # Lista de dados desordenados
    dados = [42, 78, 24, 63, 27, 9, 34, 51, 21]
    
    print("Lista original:")
    print(dados)
    
    # Chama o Quick Sort para ordenar a lista completa
    quickSort(dados, 0, len(dados) - 1)
    
    print("\nLista ordenada:")
    print(dados)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()