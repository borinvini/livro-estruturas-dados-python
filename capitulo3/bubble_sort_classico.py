def bubble_sort(dados):

    tam = len(dados)
    
    # Percorre o conjunto de dados
    for v in range(0, tam, 1):

        # Compara elementos adjacentes
        for i in range(0, tam-1, 1):

            if dados[i] > dados[i+1]:
                # Troca os elementos de posição
                aux = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = aux

def main():
    # Define a lista de dados desordenada
    dados = [5, 4, 2, 1, 8]
    
    print("Lista original:", dados)
    
    # Ordena a lista usando Bubble Sort
    bubble_sort(dados)
    
    print("Lista ordenada:", dados)

# Ponto de entrada do programa
if __name__ == "__main__":
    main()