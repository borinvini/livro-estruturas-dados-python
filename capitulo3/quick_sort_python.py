def quickSort(dados):
    """
    Implementa o Quick Sort de forma "pythônica" usando list comprehensions.
    
    Parâmetros:
        dados: lista a ser ordenada
        
    Retorna:
        Uma nova lista ordenada
    """
    # Caso base: lista vazia ou com um único elemento já está ordenada
    if len(dados) < 2:
        return dados
    else:
        # Escolhe o primeiro elemento como pivô
        pivo = dados[0]
        
        # Cria lista com elementos menores ou iguais ao pivô
        menores = [elemento for elemento in dados[1:] if elemento <= pivo]
        
        # Cria lista com elementos maiores que o pivô
        maiores = [elemento for elemento in dados[1:] if elemento > pivo]
        
        # Conquista: ordena recursivamente e concatena os resultados
        return quickSort(menores) + [pivo] + quickSort(maiores)


def main():
    """
    Função principal que demonstra o uso do Quick Sort pythônico.
    """
    # Lista de dados desordenados
    dados = [50, 25, 92, 16, 76, 30, 43, 54, 13]
    
    print("Lista original:")
    print(dados)
    
    # Chama o Quick Sort e recebe a lista ordenada
    dados_ordenados = quickSort(dados)
    
    print("\nLista ordenada:")
    print(dados_ordenados)
    
    # Demonstração com outros tipos de dados
    print("\n--- Outros exemplos ---")
    
    # Ordenando strings
    nomes = ["Maria", "João", "Ana", "Carlos", "Beatriz"]
    print(f"\nNomes originais: {nomes}")
    print(f"Nomes ordenados: {quickSort(nomes)}")
    
    # Ordenando números negativos
    numeros = [3, -1, 4, -5, 2, 0, -3]
    print(f"\nNúmeros originais: {numeros}")
    print(f"Números ordenados: {quickSort(numeros)}")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()