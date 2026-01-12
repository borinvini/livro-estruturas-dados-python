def merge_sort(dados):

    # Condição de parada: se a lista tem 1 ou 0 elementos, já está ordenada
    if len(dados) > 1:
        # Divide a lista ao meio
        meio = len(dados) // 2
        esquerda = dados[:meio]
        direita = dados[meio:]
        
        # Recursivamente ordena as duas metades
        merge_sort(esquerda)
        merge_sort(direita)
        
        # Intercala/mescla as duas metades ordenadas
        i = 0  # Índice para percorrer a sublista esquerda
        j = 0  # Índice para percorrer a sublista direita
        k = 0  # Índice para percorrer a lista original
        
        # Compara elementos das duas sublistas e intercala na ordem correta
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                dados[k] = esquerda[i]
                i += 1
            else:
                dados[k] = direita[j]
                j += 1
            k += 1
        
        # Copia os elementos restantes da sublista esquerda (se houver)
        while i < len(esquerda):
            dados[k] = esquerda[i]
            i += 1
            k += 1
        
        # Copia os elementos restantes da sublista direita (se houver)
        while j < len(direita):
            dados[k] = direita[j]
            j += 1
            k += 1

def main():
    """
    Função principal que demonstra o uso do algoritmo Merge Sort.
    """
    # Lista de dados desordenados
    dados = [38, 27, 82, 15, 63, 41, 56, 74]
    
    print("=== Demonstração do Algoritmo Merge Sort ===\n")
    print(f"Lista original: {dados}")
    
    # Aplica o algoritmo de ordenação
    merge_sort(dados)
    
    print(f"Lista ordenada: {dados}")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()