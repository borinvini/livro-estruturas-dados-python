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
    # DFS COM PILHA EXPLÍCITA (VERSÃO ITERATIVA)
    # ============================================================
    
    def dfs(self, inicio):
        """
        Realiza a Busca em Profundidade (DFS) usando uma pilha.
        
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
        
        # PILHA EXPLÍCITA - usamos uma lista Python
        # append() = push (empilhar)
        # pop() = pop (desempilhar)
        pilha = []
        
        # Empilha o vértice inicial
        pilha.append(self.vertices[inicio])
        print(f"PUSH: {inicio}")
        print(f"Pilha: {[v.valor for v in pilha]}")
        print("-" * 40)
        
        while pilha:  # Enquanto a pilha não estiver vazia
            # Desempilha o vértice do topo
            vertice_atual = pilha.pop()
            print(f"POP: {vertice_atual.valor}")
            
            # Se já foi visitado, ignora e continua
            if vertice_atual.valor in visitados:
                print(f"  (já visitado, ignorando)")
                print(f"Pilha: {[v.valor for v in pilha]}")
                print("-" * 40)
                continue
            
            # Marca como visitado e registra na ordem
            visitados.add(vertice_atual.valor)
            ordem_visita.append(vertice_atual.valor)
            print(f"  ✓ Visitando: {vertice_atual.valor}")
            
            # Empilha todos os vizinhos não visitados
            # Percorre a lista encadeada de adjacentes
            atual = vertice_atual.adjacentes.head
            while atual is not None:
                vizinho = atual.vertice
                
                if vizinho.valor not in visitados:
                    pilha.append(vizinho)
                    print(f"  PUSH: {vizinho.valor}")
                
                atual = atual.next
            
            print(f"Pilha: {[v.valor for v in pilha]}")
            print("-" * 40)
        
        return ordem_visita