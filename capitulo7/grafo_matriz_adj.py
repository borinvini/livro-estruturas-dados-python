class GrafoMatriz:
    """Representa um grafo não direcionado usando matriz de adjacência."""
    
    def __init__(self):
        self.vertices = []          # Lista com os rótulos dos vértices
        self.indices = {}           # Mapeia rótulo → índice na matriz
        self.matriz = []            # Matriz de adjacência
    
    def adicionar_vertice(self, valor):
        """Adiciona um novo vértice ao grafo."""
        if valor not in self.indices:
            self.indices[valor] = len(self.vertices)
            self.vertices.append(valor)
            
            # Expande a matriz: adiciona coluna em cada linha existente
            for linha in self.matriz:
                linha.append(0)
            
            # Adiciona nova linha com zeros
            self.matriz.append([0] * len(self.vertices))
    
    def adicionar_aresta(self, origem, destino):
        """Adiciona uma aresta entre dois vértices."""
        # Cria os vértices se ainda não existirem
        if origem not in self.indices:
            self.adicionar_vertice(origem)
        if destino not in self.indices:
            self.adicionar_vertice(destino)
        
        # Obtém os índices dos vértices
        i = self.indices[origem]
        j = self.indices[destino]
        
        # Marca a conexão (grafo não direcionado = matriz simétrica)
        self.matriz[i][j] = 1
        self.matriz[j][i] = 1
    
    def exibir(self):
        """Exibe a matriz de adjacência formatada."""
        # Cabeçalho com os rótulos das colunas
        print("    ", end="")
        for v in self.vertices:
            print(f" {v} ", end="")
        print("\n    " + "---" * len(self.vertices))
        
        # Linhas da matriz com rótulo à esquerda
        for i, linha in enumerate(self.matriz):
            print(f" {self.vertices[i]} |", end="")
            for valor in linha:
                print(f" {valor} ", end="")
            print()


if __name__ == "__main__":
    # Cria o grafo
    grafo = GrafoMatriz()
    
    # Adiciona as arestas (os vértices são criados automaticamente)
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("A", "E")
    grafo.adicionar_aresta("B", "C")
    grafo.adicionar_aresta("C", "D")
    grafo.adicionar_aresta("C", "E")
    
    # Exibe a estrutura
    print("Matriz de Adjacência:")
    print("=" * 25)
    grafo.exibir()
