class Vertice:
    """Representa um vértice (nó) do grafo."""
    
    def __init__(self, valor):
        self.valor = valor
        self.adjacentes = []


class Grafo:
    """Representa um grafo não direcionado 
    usando lista de adjacência."""
    
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, valor):
        """Adiciona um novo vértice ao grafo."""
        if valor not in self.vertices:
            self.vertices[valor] = Vertice(valor)
        return self.vertices[valor]
    
    def adicionar_aresta(self, origem, destino):
        """Adiciona uma aresta entre dois vértices."""
        if origem not in self.vertices:
            self.adicionar_vertice(origem)
        if destino not in self.vertices:
            self.adicionar_vertice(destino)
        
        self.vertices[origem].adjacentes.append(self.vertices[destino])
        self.vertices[destino].adjacentes.append(self.vertices[origem])
    
    def exibir(self):
        """Exibe a lista de adjacência do grafo."""
        for valor, vertice in self.vertices.items():
            vizinhos = [v.valor for v in vertice.adjacentes]
            print(f"{valor} → {vizinhos}")


if __name__ == "__main__":
    # Cria o grafo
    grafo = Grafo()
    
    # Adiciona as arestas 
    # (os vértices são criados automaticamente)
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("A", "E")
    grafo.adicionar_aresta("B", "C")
    grafo.adicionar_aresta("C", "D")
    grafo.adicionar_aresta("C", "E")
    
    # Exibe a estrutura
    print("Lista de Adjacência:")
    print("-" * 20)
    grafo.exibir()