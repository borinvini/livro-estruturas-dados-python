class Node:
    """Nó da lista encadeada de adjacências (com peso)."""
    
    def __init__(self, vertice=None, peso=0):
        self.vertice = vertice  # Referência para o vértice adjacente
        self.peso = peso        # Peso da aresta até este vértice
        self.next = None        # Próximo nó na lista de adjacências


class ListaAdjacencia:
    """Lista encadeada que armazena os vértices adjacentes e seus pesos."""
    
    def __init__(self):
        self.head = None
    
    def inserir_no_inicio(self, vertice, peso):
        """Insere um vértice adjacente no início da lista com seu peso."""
        novo_nodo = Node(vertice, peso)
        novo_nodo.next = self.head
        self.head = novo_nodo
    
    def exibir(self):
        """Retorna uma lista de tuplas (valor, peso) dos adjacentes."""
        resultado = []
        atual = self.head
        while atual is not None:
            resultado.append((atual.vertice.valor, atual.peso))
            atual = atual.next
        return resultado
    
    def obter_vizinhos(self):
        """Retorna lista de tuplas (vertice, peso) para uso no Dijkstra."""
        vizinhos = []
        atual = self.head
        while atual is not None:
            vizinhos.append((atual.vertice, atual.peso))
            atual = atual.next
        return vizinhos


class Vertice:
    """Representa um vértice (nó) do grafo."""
    
    def __init__(self, valor):
        self.valor = valor
        self.adjacentes = ListaAdjacencia()


class GrafoPonderado:
    """Representa um grafo não direcionado e ponderado usando lista de adjacência."""
    
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, valor):
        """Adiciona um novo vértice ao grafo."""
        if valor not in self.vertices:
            self.vertices[valor] = Vertice(valor)
        return self.vertices[valor]
    
    def adicionar_aresta(self, origem, destino, peso):
        """Adiciona uma aresta ponderada entre dois vértices."""
        if origem not in self.vertices:
            self.adicionar_vertice(origem)
        if destino not in self.vertices:
            self.adicionar_vertice(destino)
        
        # Conecta usando a lista encadeada (bidirecional)
        self.vertices[origem].adjacentes.inserir_no_inicio(
            self.vertices[destino], peso
        )
        self.vertices[destino].adjacentes.inserir_no_inicio(
            self.vertices[origem], peso
        )
    
    def exibir(self):
        """Exibe a lista de adjacência do grafo com os pesos."""
        for valor in sorted(self.vertices.keys()):
            vertice = self.vertices[valor]
            vizinhos = vertice.adjacentes.exibir()
            # Ordena por nome do vértice e formata como "B(4)"
            vizinhos_ordenados = sorted(vizinhos, key=lambda x: x[0])
            formatado = [f"{v}({p})" for v, p in vizinhos_ordenados]
            print(f"{valor} → {formatado}")
    
    def dijkstra(self, origem):
        """
        Algoritmo de Dijkstra para encontrar o caminho mais curto
        de um vértice origem para todos os outros vértices.
        
        Retorna dois dicionários:
        - distancias: menor distância da origem até cada vértice
        - predecessores: vértice anterior no caminho mais curto
        """
        # Inicialização
        infinito = float('inf')
        distancias = {v: infinito for v in self.vertices}
        predecessores = {v: None for v in self.vertices}
        visitados = set()
        
        # Distância da origem para ela mesma é zero
        distancias[origem] = 0
        
        # Enquanto houver vértices não visitados
        while len(visitados) < len(self.vertices):
            # Encontra o vértice não visitado com menor distância
            # (Esta é a versão didática - sem heap)
            vertice_atual = None
            menor_distancia = infinito
            
            for v in self.vertices:
                if (v not in visitados and 
                distancias[v] < menor_distancia):
                    menor_distancia = distancias[v]
                    vertice_atual = v
            
            # Se não encontrou vértice alcançável, encerra
            if vertice_atual is None:
                break
            
            # Marca como visitado
            visitados.add(vertice_atual)
            
            # Relaxamento: atualiza distâncias dos vizinhos
            vizinhos = self.vertices[vertice_atual]\
                .adjacentes.obter_vizinhos()
            
            for vizinho, peso in vizinhos:
                if vizinho.valor not in visitados:
                    nova_distancia = distancias[vertice_atual] + peso
                    
                    # Se encontrou caminho mais curto, atualiza
                    if nova_distancia < distancias[vizinho.valor]:
                        distancias[vizinho.valor] = nova_distancia
                        predecessores[vizinho.valor] = vertice_atual
        
        return distancias, predecessores
    
    def caminho_mais_curto(self, origem, destino):
        """
        Encontra o caminho mais curto entre origem e destino.
        Retorna o caminho (lista de vértices) e a distância total.
        """
        distancias, predecessores = self.dijkstra(origem)
        
        # Reconstrói o caminho do destino até a origem
        caminho = []
        atual = destino
        
        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]
        
        # Inverte para ter o caminho da origem ao destino
        caminho.reverse()
        
        # Verifica se existe caminho
        if distancias[destino] == float('inf'):
            return None, float('inf')
        
        return caminho, distancias[destino]
    
    def exibir_dijkstra(self, origem):
        """Exibe os resultados do Dijkstra de forma formatada."""
        distancias, predecessores = self.dijkstra(origem)
        
        print(f"\n{'='*50}")
        print(f"Dijkstra a partir do vértice '{origem}'")
        print(f"{'='*50}")
        print(f"{'Vértice':<10} {'Distância':<12} {'Predecessor':<12}")
        print(f"{'-'*34}")
        
        for v in sorted(self.vertices.keys()):
            dist = distancias[v] if distancias[v] != float('inf') else "∞"
            pred = predecessores[v] if predecessores[v] else "-"
            print(f"{v:<10} {str(dist):<12} {pred:<12}")


# ============================================================
# DEMONSTRAÇÃO
# ============================================================
if __name__ == "__main__":
    grafo = GrafoPonderado()
    
    # Grafo da figura:
    #
    #    V0 ----(2)---- V1
    #    |  \           |
    #   (2)   \(5)     (4)
    #    |      \       |
    #    V3 -----(5)--- V2
    #
    # Nota: V1-V3 tem peso 5, não há aresta direta V2-V3
    
    grafo.adicionar_aresta(0, 1, 2)   # V0 - V1: peso 2
    grafo.adicionar_aresta(0, 3, 2)   # V0 - V3: peso 2
    grafo.adicionar_aresta(1, 2, 4)   # V1 - V2: peso 4
    grafo.adicionar_aresta(1, 3, 5)   # V1 - V3: peso 5
    
    print("Lista de Adjacência (Grafo Ponderado):")
    print("-" * 40)
    grafo.exibir()
    
    # Executando Dijkstra a partir do vértice 0
    grafo.exibir_dijkstra(0)
    
    # Encontrando caminhos específicos
    print(f"\n{'='*50}")
    print("Caminhos mais curtos a partir do vértice 0:")
    print(f"{'='*50}")
    
    for destino in sorted(grafo.vertices.keys()):
        if destino != 0:
            caminho, distancia = grafo.caminho_mais_curto(0, destino)
            caminho_str = " → ".join(str(v) for v in caminho)
            print(f"0 até {destino}: {caminho_str} (distância: {distancia})")