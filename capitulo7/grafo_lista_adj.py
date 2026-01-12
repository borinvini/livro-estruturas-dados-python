class Node:
    """Nó da lista encadeada de adjacências."""
    
    def __init__(self, vertice=None):
        self.vertice = vertice  # Referência para o vértice adjacente
        self.next = None        # Próximo nó na lista de adjacências


class ListaAdjacencia:
    """Lista encadeada que armazena os vértices adjacentes."""
    
    def __init__(self):
        self.head = None
    
    def inserir_no_inicio(self, vertice):
        """Insere um vértice adjacente no início da lista."""
        novo_nodo = Node(vertice)
        novo_nodo.next = self.head
        self.head = novo_nodo
    
    def exibir(self):
        """Retorna uma string com os adjacentes."""
        resultado = []
        atual = self.head
        while atual is not None:
            resultado.append(atual.vertice.valor)
            atual = atual.next
        return resultado


class Vertice:
    """Representa um vértice (nó) do grafo."""
    
    def __init__(self, valor):
        self.valor = valor
        # Lista encadeada de adjacentes
        self.adjacentes = ListaAdjacencia()  


class Grafo:
    """Representa um grafo não direcionado usando lista de adjacência."""
    
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
        
        # Conecta usando a lista encadeada
        (self.vertices[origem].adjacentes
        .inserir_no_inicio(self.vertices[destino]))
        (self.vertices[destino]
        .adjacentes.inserir_no_inicio(self.vertices[origem]))
    
    def exibir(self):
        """Exibe a lista de adjacência do grafo em ordem alfabética."""
        for valor in sorted(self.vertices.keys()):
            vertice = self.vertices[valor]
            vizinhos = sorted(vertice.adjacentes.exibir())
            print(f"{valor} → {vizinhos}")


if __name__ == "__main__":
    grafo = Grafo()
    
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("A", "E")
    grafo.adicionar_aresta("B", "C")
    grafo.adicionar_aresta("C", "D")
    grafo.adicionar_aresta("C", "E")
    
    print("Lista de Adjacência (com Linked List):")
    print("-" * 40)
    grafo.exibir()