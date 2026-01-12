class Node:
    def __init__(self, dado=None):
        self.dado = dado    # Armazena o dado do nodo
        self.left = None    # Referência para o filho da esquerda
        self.right = None   # Referência para o filho da direita


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inserir(self, dado, nodo_atual=None):
            """Insere um novo dado na árvore de forma recursiva."""
            
            # Se nodo_atual é None, verificamos se é a primeira inserção
            if nodo_atual is None:
                # Árvore vazia? O novo dado se torna a raiz
                if self.root is None:
                    self.root = Node(dado)
                    return
                # Árvore não vazia? Começamos a busca pela raiz
                return self.inserir(dado, self.root)
            
            # Comparamos o dado com o nodo atual
            
            # Dado menor? Vai para a esquerda
            if dado < nodo_atual.dado:
                # Já existe filho à esquerda? Desce recursivamente
                if nodo_atual.left:
                    self.inserir(dado, nodo_atual.left)
                else:
                    # Não existe filho? Insere aqui
                    nodo_atual.left = Node(dado)
            
            # Dado maior ou igual? Vai para a direita
            else:
                # Já existe filho à direita? Desce recursivamente
                if nodo_atual.right:
                    self.inserir(dado, nodo_atual.right)
                else:
                    # Não existe filho? Insere aqui
                    nodo_atual.right = Node(dado)

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

    def mostrar(self, nodo=None, prefixo="", is_left=True, is_root=True):
        """Exibe a árvore de forma visual no terminal."""
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
            self.mostrar(nodo.right, novo_prefixo, False, False)

        if nodo.left is not None:
            novo_prefixo = prefixo + ("    " if not is_root and is_left else "│   ")
            print(f"{prefixo}{'    ' if not is_root and is_left else '│   ' if not is_root else '    '}└── ({nodo.left.dado})")
            self.mostrar(nodo.left, novo_prefixo, True, False)

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
    print("       ARVORE BINARIA DE BUSCA - MENU INTERATIVO")
    print("=" * 60)
    print("\n1 - Carregar exemplo pronto")
    print("2 - Inserir valor manualmente")
    print("3 - Visualizar arvore")
    print("4 - Mostrar percursos em profundidade")
    print("5 - Mostrar percurso em largura")
    print("6 - Mostrar todos os percursos")
    print("7 - Reiniciar arvore (limpar)")
    print("8 - Limpar tela")
    print("0 - Sair")
    print("=" * 60)


def carregar_exemplo(arvore):
    """Carrega um exemplo pronto na árvore."""
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arvore.inserir(valor)
    print(f"\nExemplo carregado com sucesso!")
    print(f"Valores inseridos: {valores}")


def inserir_valor(arvore):
    """Insere um único valor na árvore."""
    try:
        valor = int(input("\nDigite o valor inteiro a ser inserido: "))
        arvore.inserir(valor)
        print(f"Valor {valor} inserido com sucesso!")
    except ValueError:
        print("Erro: Digite apenas numeros inteiros.")


def visualizar_arvore(arvore):
    """Visualiza a estrutura da árvore."""
    print("\n" + "=" * 60)
    print("           VISUALIZACAO DA ARVORE")
    print("=" * 60 + "\n")
    arvore.mostrar()
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
    
    visualizar_arvore(arvore)
    mostrar_percursos_profundidade(arvore)
    mostrar_percurso_largura(arvore)


def reiniciar_arvore(arvore):
    """Reinicia a árvore, removendo todos os elementos."""
    confirmacao = input("\nTem certeza que deseja limpar a arvore? (s/n): ")
    if confirmacao.lower() == 's':
        arvore.root = None
        print("Arvore reiniciada com sucesso!")
    else:
        print("Operacao cancelada.")


if __name__ == "__main__":
    arvore = BinarySearchTree()
    
    print("\nBem-vindo ao Sistema de Arvore Binaria de Busca!")
    print("Explore as operacoes e percursos de forma interativa.\n")
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opcao: ").strip()
            
            if opcao == "1":
                carregar_exemplo(arvore)
            
            elif opcao == "2":
                inserir_valor(arvore)
            
            elif opcao == "3":
                visualizar_arvore(arvore)
            
            elif opcao == "4":
                mostrar_percursos_profundidade(arvore)
            
            elif opcao == "5":
                mostrar_percurso_largura(arvore)
            
            elif opcao == "6":
                mostrar_todos_percursos(arvore)
            
            elif opcao == "7":
                reiniciar_arvore(arvore)
            
            elif opcao == "8":
                limpar_tela()
            
            elif opcao == "0":
                print("\nObrigado por usar o sistema! Ate logo!\n")
                break
            
            else:
                print("\nOpcao invalida! Escolha um numero de 0 a 8.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido. Ate logo!\n")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")