def bubble_sort(dados):

    tam = len(dados)
    
    # Percorre o conjunto de dados
    for v in range(tam):
        # Assume que a lista está ordenada (otimista!)
        houve_troca = False
        
        # Compara elementos adjacentes
        # Note que reduzimos o range a cada iteração (tam-1-v)
        # pois os maiores elementos já "borbulham" para o final
        for i in range(tam - 1 - v):
            
            # Se o elemento atual é maior que o próximo, troca!
            if dados[i] > dados[i + 1]:
                # Troca os elementos de posição
                dados[i], dados[i + 1] = dados[i + 1], dados[i]
                
                # Marca que houve pelo menos uma troca
                houve_troca = True
        
        # Otimização: se não houve troca, a lista já está ordenada
        # Não precisa continuar as iterações!
        if not houve_troca:
            print(f"Lista ordenada na {v + 1}ª passada!")
            print(f"Encerrando precocemente.")
            break

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