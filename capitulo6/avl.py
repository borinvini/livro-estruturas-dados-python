class Node:
    def __init__(self, dado=None):
        self.dado = dado    # Armazena o dado do nodo
        self.left = None    # Referência para o filho da esquerda
        self.right = None   # Referência para o filho da direita
        self.altura = 1     # Altura do nodo (novo atributo para AVL)


class AVLTree:
    def __init__(self):
        self.root = None

    # ==================== MÉTODOS AUXILIARES AVL ====================

    def _altura(self, nodo):
        """Retorna a altura de um nodo. Nodo None tem altura 0."""
        if nodo is None:
            return 0
        return nodo.altura

    def _fator_balanceamento(self, nodo):
        """
        Calcula o fator de balanceamento de um nodo.
        FB = altura(esquerda) - altura(direita)
        
        Valores possíveis em uma AVL balanceada: -1, 0, +1
        Se FB < -1 ou FB > +1, a árvore precisa de rotação.
        """
        if nodo is None:
            return 0
        return self._altura(nodo.left) - self._altura(nodo.right)

    def _atualizar_altura(self, nodo):
        """Atualiza a altura de um nodo baseado nas alturas dos filhos."""
        if nodo is not None:
            nodo.altura = 1 + max(self._altura(nodo.left), 
                                  self._altura(nodo.right))

    # ==================== ROTAÇÕES ====================

    def _rotacao_direita(self, y):
        r"""
        Rotação simples à direita (caso Esquerda-Esquerda).
        
              y                    x
             / \                  / \
            x   T3    -->       T1   y
           / \                      / \
          T1  T2                   T2  T3
        
        Retorna a nova raiz da subárvore (x).
        """
        x = y.left           # x será a nova raiz
        T2 = x.right         # T2 é a subárvore direita de x
        
        # Realiza a rotação
        x.right = y          # y se torna filho direito de x
        y.left = T2          # T2 se torna filho esquerdo de y
        
        # Atualiza as alturas (ordem importa: y primeiro, depois x)
        self._atualizar_altura(y)
        self._atualizar_altura(x)
        
        return x  # Nova raiz da subárvore

    def _rotacao_esquerda(self, x):
        r"""
        Rotação simples à esquerda (caso Direita-Direita).
        
            x                       y
           / \                     / \
          T1  y       -->         x   T3
             / \                 / \
            T2  T3              T1  T2
        
        Retorna a nova raiz da subárvore (y).
        """
        y = x.right          # y será a nova raiz
        T2 = y.left          # T2 é a subárvore esquerda de y
        
        # Realiza a rotação
        y.left = x           # x se torna filho esquerdo de y
        x.right = T2         # T2 se torna filho direito de x
        
        # Atualiza as alturas (ordem importa: x primeiro, depois y)
        self._atualizar_altura(x)
        self._atualizar_altura(y)
        
        return y  # Nova raiz da subárvore

    def _balancear(self, nodo):
        """
        Verifica e corrige o balanceamento de um nodo.
        
        Existem 4 casos de desbalanceamento:
        
        1. Esquerda-Esquerda (FB > 1 e FB_esq >= 0): Rotação direita
        2. Esquerda-Direita (FB > 1 e FB_esq < 0): Rotação esquerda-direita
        3. Direita-Direita (FB < -1 e FB_dir <= 0): Rotação esquerda
        4. Direita-Esquerda (FB < -1 e FB_dir > 0): Rotação direita-esquerda
        
        Retorna o nodo (possivelmente um novo) após balanceamento.
        """
        # Atualiza a altura do nodo atual
        self._atualizar_altura(nodo)
        
        # Calcula o fator de balanceamento
        fb = self._fator_balanceamento(nodo)
        
        # Caso 1: Esquerda-Esquerda (Left-Left)
        # Desbalanceado à esquerda e inserção foi à esquerda do filho esquerdo
        if fb > 1 and self._fator_balanceamento(nodo.left) >= 0:
            return self._rotacao_direita(nodo)
        
        # Caso 2: Esquerda-Direita (Left-Right)
        # Desbalanceado à esquerda e inserção foi à direita do filho esquerdo
        if fb > 1 and self._fator_balanceamento(nodo.left) < 0:
            nodo.left = self._rotacao_esquerda(nodo.left)  # Rotação dupla
            return self._rotacao_direita(nodo)
        
        # Caso 3: Direita-Direita (Right-Right)
        # Desbalanceado à direita e inserção foi à direita do filho direito
        if fb < -1 and self._fator_balanceamento(nodo.right) <= 0:
            return self._rotacao_esquerda(nodo)
        
        # Caso 4: Direita-Esquerda (Right-Left)
        # Desbalanceado à direita e inserção foi à esquerda do filho direito
        if fb < -1 and self._fator_balanceamento(nodo.right) > 0:
            nodo.right = self._rotacao_direita(nodo.right)  # Rotação dupla
            return self._rotacao_esquerda(nodo)
        
        # Nodo já está balanceado
        return nodo

    # ==================== INSERÇÃO AVL ====================

    def inserir(self, dado, nodo_atual=None):
        """
        Insere um novo dado na árvore AVL de forma recursiva.
        Após a inserção, verifica e corrige o balanceamento.
        """
        # Se nodo_atual é None, verificamos se é a primeira inserção
        if nodo_atual is None:
            # Árvore vazia? O novo dado se torna a raiz
            if self.root is None:
                self.root = Node(dado)
                return None
            # Árvore não vazia? Começamos a busca pela raiz
            self.root = self.inserir(dado, self.root)
            return None
        
        # Caso base: encontrou posição vazia, cria novo nodo
        if nodo_atual.dado is None:
            return Node(dado)
        
        # Busca recursiva pela posição correta
        if dado < nodo_atual.dado:
            if nodo_atual.left is None:
                nodo_atual.left = Node(dado)
            else:
                nodo_atual.left = self.inserir(dado, nodo_atual.left)
        else:
            if nodo_atual.right is None:
                nodo_atual.right = Node(dado)
            else:
                nodo_atual.right = self.inserir(dado, nodo_atual.right)
        
        # Após inserção, balanceia o nodo atual (backtracking)
        return self._balancear(nodo_atual)

    # ==================== REMOÇÃO AVL ====================

    def _encontrar_minimo(self, nodo):
        """Encontra o nodo com menor valor em uma subárvore."""
        atual = nodo
        while atual.left is not None:
            atual = atual.left
        return atual

    def remover(self, dado):
        """Remove um dado da árvore AVL mantendo o balanceamento."""
        self.root = self._remover_recursivo(self.root, dado)

    def _remover_recursivo(self, nodo, dado):
        """Método interno recursivo para remoção com balanceamento."""
        
        # Caso base: nodo não encontrado
        if nodo is None:
            return nodo
        
        # Busca pelo nodo a ser removido
        if dado < nodo.dado:
            nodo.left = self._remover_recursivo(nodo.left, dado)
        elif dado > nodo.dado:
            nodo.right = self._remover_recursivo(nodo.right, dado)
        else:
            # Encontrou o nodo a ser removido
            
            # Caso 1: Nodo folha ou com apenas um filho
            if nodo.left is None:
                return nodo.right
            elif nodo.right is None:
                return nodo.left
            
            # Caso 2: Nodo com dois filhos
            # Encontra o sucessor in-order (menor da subárvore direita)
            sucessor = self._encontrar_minimo(nodo.right)
            nodo.dado = sucessor.dado
            nodo.right = self._remover_recursivo(nodo.right, sucessor.dado)
        
        # Após remoção, balanceia o nodo atual
        return self._balancear(nodo)

    # ==================== BUSCA ====================

    def buscar(self, dado, nodo="inicio"):
        """Busca um dado na árvore. Retorna True se encontrar."""
        if nodo == "inicio":
            nodo = self.root
        
        if nodo is None:
            return False
        
        if dado == nodo.dado:
            return True
        elif dado < nodo.dado:
            return self.buscar(dado, nodo.left)
        else:
            return self.buscar(dado, nodo.right)

    # ==================== PERCURSOS EM PROFUNDIDADE ====================

    def em_ordem(self, nodo="inicio"):
        """
        Percurso em ordem (in-order): esquerda -> raiz -> direita
        Retorna os elementos em ordem crescente.
        """
        if nodo == "inicio":
            nodo = self.root
        
        if nodo is None:
            return []
        
        resultado = []
        resultado += self.em_ordem(nodo.left)   # Visita subárvore esquerda
        resultado.append(nodo.dado)              # Visita a raiz
        resultado += self.em_ordem(nodo.right)  # Visita subárvore direita
        return resultado

    def pre_ordem(self, nodo="inicio"):
        """
        Percurso pré-ordem (pre-order): raiz -> esquerda -> direita
        Útil para copiar a árvore.
        """
        if nodo == "inicio":
            nodo = self.root
        
        if nodo is None:
            return []
        
        resultado = []
        resultado.append(nodo.dado)              # Visita a raiz
        resultado += self.pre_ordem(nodo.left)   # Visita subárvore esquerda
        resultado += self.pre_ordem(nodo.right)  # Visita subárvore direita
        return resultado

    def pos_ordem(self, nodo="inicio"):
        """
        Percurso pós-ordem (post-order): esquerda -> direita -> raiz
        Útil para deletar a árvore.
        """
        if nodo == "inicio":
            nodo = self.root
        
        if nodo is None:
            return []
        
        resultado = []
        resultado += self.pos_ordem(nodo.left)   # Visita subárvore esquerda
        resultado += self.pos_ordem(nodo.right)  # Visita subárvore direita
        resultado.append(nodo.dado)              # Visita a raiz
        return resultado

    # ==================== PERCURSO EM LARGURA ====================

    def em_largura(self):
        """
        Percurso em largura (level-order): nível por nível.
        Utiliza uma fila para visitar os nós.
        """
        if self.root is None:
            return []
        
        resultado = []
        fila = [self.root]  # Inicia a fila com a raiz
        
        while fila:
            nodo_atual = fila.pop(0)         # Remove o primeiro da fila
            resultado.append(nodo_atual.dado)
            
            if nodo_atual.left:              # Adiciona filho esquerdo à fila
                fila.append(nodo_atual.left)
            if nodo_atual.right:             # Adiciona filho direito à fila
                fila.append(nodo_atual.right)
        
        return resultado

    # ==================== MÉTODOS DE INFORMAÇÃO AVL ====================

    def obter_altura_arvore(self):
        """Retorna a altura total da árvore."""
        return self._altura(self.root)

    def verificar_balanceamento(self, nodo="inicio"):
        """
        Verifica se a árvore está balanceada.
        Retorna uma tupla (balanceada, info) com detalhes.
        """
        if nodo == "inicio":
            nodo = self.root
        
        if nodo is None:
            return True, []
        
        info = []
        fb = self._fator_balanceamento(nodo)
        
        if abs(fb) > 1:
            info.append(f"Nodo {nodo.dado}: FB={fb} (DESBALANCEADO)")
        else:
            info.append(f"Nodo {nodo.dado}: FB={fb}")
        
        # Verifica subárvores
        bal_esq, info_esq = self.verificar_balanceamento(nodo.left)
        bal_dir, info_dir = self.verificar_balanceamento(nodo.right)
        
        info.extend(info_esq)
        info.extend(info_dir)
        
        balanceada = abs(fb) <= 1 and bal_esq and bal_dir
        return balanceada, info

    def mostrar(self, nodo=None, prefixo="", is_left=True, is_root=True):
        """Exibe a árvore de forma visual no terminal com informações AVL."""
        if is_root:
            nodo = self.root
            if nodo is None:
                print("Árvore vazia")
                return
            fb = self._fator_balanceamento(nodo)
            print(f"({nodo.dado}) [h={nodo.altura}, fb={fb}]")
        
        if nodo is None:
            return

        if nodo.right is not None:
            novo_prefixo = prefixo + ("│   " if not is_root and is_left else "    ")
            fb = self._fator_balanceamento(nodo.right)
            print(f"{prefixo}{'│   ' if not is_root and is_left else '    '}┌── ({nodo.right.dado}) [h={nodo.right.altura}, fb={fb}]")
            self.mostrar(nodo.right, novo_prefixo, False, False)

        if nodo.left is not None:
            novo_prefixo = prefixo + ("    " if not is_root and is_left else "│   ")
            fb = self._fator_balanceamento(nodo.left)
            print(f"{prefixo}{'    ' if not is_root and is_left else '│   ' if not is_root else '    '}└── ({nodo.left.dado}) [h={nodo.left.altura}, fb={fb}]")
            self.mostrar(nodo.left, novo_prefixo, True, False)

    def mostrar_simples(self, nodo=None, prefixo="", is_left=True, is_root=True):
        """Exibe a árvore de forma visual simples (sem info AVL)."""
        if is_root:
            nodo = self.root
            if nodo is None:
                print("Árvore vazia")
                return
            print(f"({nodo.dado})")
        
        if nodo is None:
            return

        if nodo.right is not None:
            novo_prefixo = prefixo + ("│   " if not is_root and is_left else "    ")
            print(f"{prefixo}{'│   ' if not is_root and is_left else '    '}┌── ({nodo.right.dado})")
            self.mostrar_simples(nodo.right, novo_prefixo, False, False)

        if nodo.left is not None:
            novo_prefixo = prefixo + ("    " if not is_root and is_left else "│   ")
            print(f"{prefixo}{'    ' if not is_root and is_left else '│   ' if not is_root else '    '}└── ({nodo.left.dado})")
            self.mostrar_simples(nodo.left, novo_prefixo, True, False)

    def esta_vazia(self):
        """Verifica se a árvore está vazia."""
        return self.root is None


def limpar_tela():
    """Função auxiliar para limpar a tela."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "=" * 60)
    print("          ARVORE AVL - MENU INTERATIVO")
    print("=" * 60)
    print("\n1  - Carregar exemplo pronto")
    print("2  - Inserir valor manualmente")
    print("3  - Remover valor")
    print("4  - Buscar valor")
    print("5  - Visualizar arvore (com info AVL)")
    print("6  - Visualizar arvore (simples)")
    print("7  - Mostrar percursos em profundidade")
    print("8  - Mostrar percurso em largura")
    print("9  - Mostrar todos os percursos")
    print("10 - Verificar balanceamento")
    print("11 - Mostrar altura da arvore")
    print("12 - Demonstrar rotacoes (exemplo didatico)")
    print("13 - Reiniciar arvore (limpar)")
    print("14 - Limpar tela")
    print("0  - Sair")
    print("=" * 60)


def carregar_exemplo(arvore):
    """Carrega um exemplo pronto na árvore."""
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arvore.inserir(valor)
    print(f"\nExemplo carregado com sucesso!")
    print(f"Valores inseridos: {valores}")
    print(f"Altura da arvore: {arvore.obter_altura_arvore()}")


def inserir_valor(arvore):
    """Insere um único valor na árvore."""
    try:
        valor = int(input("\nDigite o valor inteiro a ser inserido: "))
        altura_antes = arvore.obter_altura_arvore()
        arvore.inserir(valor)
        altura_depois = arvore.obter_altura_arvore()
        print(f"Valor {valor} inserido com sucesso!")
        if altura_antes != altura_depois:
            print(f"Altura da arvore alterada: {altura_antes} -> {altura_depois}")
        else:
            print(f"Altura da arvore: {altura_depois}")
    except ValueError:
        print("Erro: Digite apenas numeros inteiros.")


def remover_valor(arvore):
    """Remove um valor da árvore."""
    if arvore.esta_vazia():
        print("\nA arvore esta vazia!")
        return
    
    try:
        valor = int(input("\nDigite o valor a ser removido: "))
        if arvore.buscar(valor):
            altura_antes = arvore.obter_altura_arvore()
            arvore.remover(valor)
            altura_depois = arvore.obter_altura_arvore()
            print(f"Valor {valor} removido com sucesso!")
            if altura_antes != altura_depois:
                print(f"Altura da arvore alterada: {altura_antes} -> {altura_depois}")
        else:
            print(f"Valor {valor} nao encontrado na arvore.")
    except ValueError:
        print("Erro: Digite apenas numeros inteiros.")


def buscar_valor(arvore):
    """Busca um valor na árvore."""
    if arvore.esta_vazia():
        print("\nA arvore esta vazia!")
        return
    
    try:
        valor = int(input("\nDigite o valor a ser buscado: "))
        if arvore.buscar(valor):
            print(f"Valor {valor} ENCONTRADO na arvore!")
        else:
            print(f"Valor {valor} NAO encontrado na arvore.")
    except ValueError:
        print("Erro: Digite apenas numeros inteiros.")


def visualizar_arvore(arvore, com_info=True):
    """Visualiza a estrutura da árvore."""
    print("\n" + "=" * 60)
    if com_info:
        print("      VISUALIZACAO DA ARVORE AVL (com altura e FB)")
    else:
        print("           VISUALIZACAO DA ARVORE AVL")
    print("=" * 60 + "\n")
    
    if com_info:
        print("Legenda: (valor) [h=altura, fb=fator de balanceamento]\n")
        arvore.mostrar()
    else:
        arvore.mostrar_simples()
    print()


def mostrar_percursos_profundidade(arvore):
    """Mostra os três percursos em profundidade."""
    if arvore.esta_vazia():
        print("\nA arvore esta vazia!")
        return
    
    print("\n" + "=" * 60)
    print("           PERCURSOS EM PROFUNDIDADE")
    print("=" * 60)
    print(f"\nEm ordem (in-order):    {arvore.em_ordem()}")
    print(f"Pre-ordem (pre-order):  {arvore.pre_ordem()}")
    print(f"Pos-ordem (post-order): {arvore.pos_ordem()}")


def mostrar_percurso_largura(arvore):
    """Mostra o percurso em largura."""
    if arvore.esta_vazia():
        print("\nA arvore esta vazia!")
        return
    
    print("\n" + "=" * 60)
    print("           PERCURSO EM LARGURA")
    print("=" * 60)
    print(f"\nEm largura (level-order): {arvore.em_largura()}")


def mostrar_todos_percursos(arvore):
    """Mostra todos os percursos de uma vez."""
    if arvore.esta_vazia():
        print("\nA arvore esta vazia!")
        return
    
    visualizar_arvore(arvore, com_info=False)
    mostrar_percursos_profundidade(arvore)
    mostrar_percurso_largura(arvore)


def verificar_balanceamento(arvore):
    """Verifica e exibe informações de balanceamento."""
    if arvore.esta_vazia():
        print("\nA arvore esta vazia!")
        return
    
    print("\n" + "=" * 60)
    print("           VERIFICACAO DE BALANCEAMENTO")
    print("=" * 60)
    
    balanceada, info = arvore.verificar_balanceamento()
    
    print("\nFatores de balanceamento por nodo:")
    for linha in info:
        print(f"  {linha}")
    
    print(f"\nStatus: {'ARVORE BALANCEADA' if balanceada else 'ARVORE DESBALANCEADA'}")


def mostrar_altura(arvore):
    """Mostra a altura da árvore."""
    print("\n" + "=" * 60)
    print("           INFORMACOES DE ALTURA")
    print("=" * 60)
    print(f"\nAltura da arvore: {arvore.obter_altura_arvore()}")
    
    if not arvore.esta_vazia():
        print(f"Quantidade de elementos: {len(arvore.em_ordem())}")


def demonstrar_rotacoes():
    """Demonstra as rotações AVL com exemplos didáticos."""
    print("\n" + "=" * 60)
    print("           DEMONSTRACAO DE ROTACOES AVL")
    print("=" * 60)
    
    # Demonstração 1: Rotação Direita (Left-Left)
    print("\n--- CASO 1: Rotacao Direita (Left-Left) ---")
    print("Inserindo: 30, 20, 10 (causa desbalanceamento LL)")
    
    avl_ll = AVLTree()
    print("\nApos inserir 30:")
    avl_ll.inserir(30)
    avl_ll.mostrar()
    
    print("\nApos inserir 20:")
    avl_ll.inserir(20)
    avl_ll.mostrar()
    
    print("\nApos inserir 10 (rotacao direita automatica):")
    avl_ll.inserir(10)
    avl_ll.mostrar()
    
    # Demonstração 2: Rotação Esquerda (Right-Right)
    print("\n--- CASO 2: Rotacao Esquerda (Right-Right) ---")
    print("Inserindo: 10, 20, 30 (causa desbalanceamento RR)")
    
    avl_rr = AVLTree()
    print("\nApos inserir 10:")
    avl_rr.inserir(10)
    avl_rr.mostrar()
    
    print("\nApos inserir 20:")
    avl_rr.inserir(20)
    avl_rr.mostrar()
    
    print("\nApos inserir 30 (rotacao esquerda automatica):")
    avl_rr.inserir(30)
    avl_rr.mostrar()
    
    # Demonstração 3: Rotação Esquerda-Direita (Left-Right)
    print("\n--- CASO 3: Rotacao Esquerda-Direita (Left-Right) ---")
    print("Inserindo: 30, 10, 20 (causa desbalanceamento LR)")
    
    avl_lr = AVLTree()
    print("\nApos inserir 30:")
    avl_lr.inserir(30)
    avl_lr.mostrar()
    
    print("\nApos inserir 10:")
    avl_lr.inserir(10)
    avl_lr.mostrar()
    
    print("\nApos inserir 20 (rotacao dupla: esquerda + direita):")
    avl_lr.inserir(20)
    avl_lr.mostrar()
    
    # Demonstração 4: Rotação Direita-Esquerda (Right-Left)
    print("\n--- CASO 4: Rotacao Direita-Esquerda (Right-Left) ---")
    print("Inserindo: 10, 30, 20 (causa desbalanceamento RL)")
    
    avl_rl = AVLTree()
    print("\nApos inserir 10:")
    avl_rl.inserir(10)
    avl_rl.mostrar()
    
    print("\nApos inserir 30:")
    avl_rl.inserir(30)
    avl_rl.mostrar()
    
    print("\nApos inserir 20 (rotacao dupla: direita + esquerda):")
    avl_rl.inserir(20)
    avl_rl.mostrar()
    
    print("\n" + "=" * 60)
    print("Demonstracao concluida!")
    print("=" * 60)


def reiniciar_arvore(arvore):
    """Reinicia a árvore, removendo todos os elementos."""
    confirmacao = input("\nTem certeza que deseja limpar a arvore? (s/n): ")
    if confirmacao.lower() == 's':
        arvore.root = None
        print("Arvore reiniciada com sucesso!")
    else:
        print("Operacao cancelada.")


if __name__ == "__main__":
    arvore = AVLTree()
    
    print("\nBem-vindo ao Sistema de Arvore AVL!")
    print("Explore as operacoes, percursos e rotacoes de forma interativa.\n")
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opcao: ").strip()
            
            if opcao == "1":
                carregar_exemplo(arvore)
            
            elif opcao == "2":
                inserir_valor(arvore)
            
            elif opcao == "3":
                remover_valor(arvore)
            
            elif opcao == "4":
                buscar_valor(arvore)
            
            elif opcao == "5":
                visualizar_arvore(arvore, com_info=True)
            
            elif opcao == "6":
                visualizar_arvore(arvore, com_info=False)
            
            elif opcao == "7":
                mostrar_percursos_profundidade(arvore)
            
            elif opcao == "8":
                mostrar_percurso_largura(arvore)
            
            elif opcao == "9":
                mostrar_todos_percursos(arvore)
            
            elif opcao == "10":
                verificar_balanceamento(arvore)
            
            elif opcao == "11":
                mostrar_altura(arvore)
            
            elif opcao == "12":
                demonstrar_rotacoes()
            
            elif opcao == "13":
                reiniciar_arvore(arvore)
            
            elif opcao == "14":
                limpar_tela()
            
            elif opcao == "0":
                print("\nObrigado por usar o sistema! Ate logo!\n")
                break
            
            else:
                print("\nOpcao invalida! Escolha um numero de 0 a 14.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido. Ate logo!\n")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")