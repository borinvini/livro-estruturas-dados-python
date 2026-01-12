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
        self.adjacentes = ListaAdjacencia()  # Lista encadeada de adjacentes


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
        self.vertices[origem].adjacentes.inserir_no_inicio(self.vertices[destino])
        self.vertices[destino].adjacentes.inserir_no_inicio(self.vertices[origem])
    
    def exibir(self):
        """Exibe a lista de adjacência do grafo."""
        for valor, vertice in self.vertices.items():
            vizinhos = vertice.adjacentes.exibir()
            print(f"{valor} → {vizinhos}")
    
    # ============================================================
    # BFS COM FILA EXPLÍCITA (VERSÃO ITERATIVA)
    # ============================================================
    
    def bfs(self, inicio):
        """
        Realiza a Busca em Largura (BFS) usando uma fila.
        
        Args:
            inicio: O valor do vértice onde a busca começa.
        
        Returns:
            Lista com a ordem de visitação dos vértices.
        """
        if inicio not in self.vertices:
            print(f"Vértice '{inicio}' não encontrado no grafo!")
            return []
        
        # Conjunto para rastrear vértices já visitados
        visitados = set()
        
        # Lista que armazenará a ordem de visitação
        ordem_visita = []
        
        # FILA EXPLÍCITA - usamos uma lista Python
        # append() = enqueue (enfileirar no final)
        # pop(0) = dequeue (desenfileirar do início)
        fila = []
        
        # Enfileira o vértice inicial e já o marca como visitado
        # Na BFS, marcamos como visitado ao ENFILEIRAR
        # Isso evita adicionar o mesmo vértice múltiplas vezes na fila
        fila.append(self.vertices[inicio])
        visitados.add(inicio)
        print(f"ENQUEUE: {inicio} (marcado como visitado)")
        print(f"Fila: {[v.valor for v in fila]}")
        print("-" * 40)
        
        while fila:  # Enquanto a fila não estiver vazia
            # Desenfileira o vértice da frente (o mais antigo)
            vertice_atual = fila.pop(0)
            print(f"DEQUEUE: {vertice_atual.valor}")
            
            # Registra na ordem de visitação
            ordem_visita.append(vertice_atual.valor)
            print(f"  ✓ Processando: {vertice_atual.valor}")
            
            # Enfileira todos os vizinhos não visitados
            # Percorre a lista encadeada de adjacentes
            atual = vertice_atual.adjacentes.head
            while atual is not None:
                vizinho = atual.vertice
                
                # Na BFS, verificamos e marcamos ao ENFILEIRAR
                if vizinho.valor not in visitados:
                    visitados.add(vizinho.valor)
                    fila.append(vizinho)
                    print(f"  ENQUEUE: {vizinho.valor}\
                          (marcado como visitado)")
                
                atual = atual.next
            
            print(f"Fila: {[v.valor for v in fila]}")
            print("-" * 40)
        
        return ordem_visita


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
    
    print("\n" + "=" * 40)
    print("BFS COM FILA EXPLÍCITA")
    print("=" * 40 + "\n")
    
    resultado = grafo.bfs("A")
    
    print(f"\nOrdem de visitação: {resultado}")