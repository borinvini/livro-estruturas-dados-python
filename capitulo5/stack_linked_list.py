class Node:
    def __init__(self, dado=None):
        self.dado = dado  # Armazena o dado do nodo
        self.next = None  # Referência para o próximo nodo


class Stack:
    """
    Implementação de Pilha (Stack) usando Lista Encadeada.
    
    A pilha segue o princípio LIFO (Last In, First Out):
    o último elemento inserido é o primeiro a ser removido.
    
    O topo da pilha corresponde ao head da lista encadeada,
    garantindo operações O(1) para push e pop.
    """
    
    def __init__(self):
        self.top = None  # Referência para o topo da pilha (equivalente ao head)
        self._size = 0   # Contador de elementos para acesso O(1) ao tamanho

    # ==================== OPERAÇÕES PRINCIPAIS ====================

    def push(self, dado):
        """
        Empilha um novo elemento no topo da pilha.
        
        Complexidade: O(1)
        
        Args:
            dado: O valor a ser empilhado
        """
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)
        
        # O próximo do novo nodo aponta para o antigo topo
        novo_nodo.next = self.top
        
        # O topo agora aponta para o novo nodo
        self.top = novo_nodo
        
        # Incrementa o contador de elementos
        self._size += 1

    def pop(self):
        """
        Desempilha e retorna o elemento do topo da pilha.
        
        Complexidade: O(1)
        
        Returns:
            O dado do elemento removido, ou None se a pilha estiver vazia
        
        Raises:
            Exibe mensagem de erro se a pilha estiver vazia
        """
        # Caso especial: pilha vazia
        if self.top is None:
            print("Erro: A pilha está vazia (Stack Underflow)")
            return None
        
        # Guarda o dado do nodo removido para retornar
        dado_removido = self.top.dado
        
        # O topo passa a apontar para o próximo nodo
        # O antigo topo será coletado pelo garbage collector
        self.top = self.top.next
        
        # Decrementa o contador de elementos
        self._size -= 1
        
        return dado_removido

    def peek(self):
        """
        Retorna o elemento do topo sem removê-lo.
        
        Complexidade: O(1)
        
        Returns:
            O dado do elemento no topo, ou None se a pilha estiver vazia
        """
        # Caso especial: pilha vazia
        if self.top is None:
            print("Erro: A pilha está vazia")
            return None
        
        # Retorna o dado do topo sem modificar a pilha
        return self.top.dado

    # ==================== MÉTODOS AUXILIARES ====================

    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        
        Complexidade: O(1)
        
        Returns:
            True se a pilha estiver vazia, False caso contrário
        """
        return self.top is None

    def size(self):
        """
        Retorna o número de elementos na pilha.
        
        Complexidade: O(1) - usa contador interno
        
        Returns:
            Número de elementos na pilha
        """
        return self._size

    def clear(self):
        """
        Remove todos os elementos da pilha.
        
        Complexidade: O(1)
        """
        self.top = None
        self._size = 0

    def display(self):
        """
        Exibe todos os elementos da pilha, do topo para a base.
        
        Complexidade: O(n)
        """
        # Caso especial: pilha vazia
        if self.top is None:
            print("Pilha vazia")
            return
        
        print("\n    ┌─────────────────┐")
        print("    │   TOPO DA PILHA │")
        print("    └────────┬────────┘")
        
        # Inicia a varredura a partir do topo
        nodo_atual = self.top
        posicao = self._size - 1
        
        # Percorre toda a pilha até o final
        while nodo_atual:
            # Indica visualmente o topo
            if nodo_atual == self.top:
                print(f"             ▼")
            print(f"    ┌─────────────────┐")
            print(f"    │ [{posicao}] {nodo_atual.dado:^10} │")
            print(f"    └─────────────────┘")
            
            nodo_atual = nodo_atual.next
            posicao -= 1
            
            if nodo_atual:
                print(f"             │")
        
        print("    ═══════════════════")
        print("        BASE DA PILHA")

    def to_list(self):
        """
        Converte a pilha em uma lista Python (do topo para a base).
        
        Complexidade: O(n)
        
        Returns:
            Lista com os elementos da pilha
        """
        elementos = []
        nodo_atual = self.top
        
        while nodo_atual:
            elementos.append(nodo_atual.dado)
            nodo_atual = nodo_atual.next
        
        return elementos


# ==================== FUNÇÕES DO MENU ====================

def exibir_menu():
    """Exibe o menu de opções para o usuário"""
    print("\n" + "=" * 50)
    print("         GERENCIADOR DE PILHA (STACK)")
    print("            Implementação com Lista")
    print("=" * 50)
    print("\n--- OPERAÇÕES PRINCIPAIS ---")
    print("1. Empilhar elemento (push)")
    print("2. Desempilhar elemento (pop)")
    print("3. Visualizar topo (peek)")
    print("\n--- VISUALIZAÇÃO ---")
    print("4. Exibir pilha completa")
    print("5. Exibir tamanho da pilha")
    print("6. Verificar se está vazia")
    print("\n--- SISTEMA ---")
    print("7. Limpar pilha")
    print("8. Carregar dados de exemplo")
    print("0. Sair")
    print("=" * 50)


def carregar_exemplo(pilha):
    """
    Carrega dados de exemplo na pilha para demonstração.
    
    Simula uma pilha de pratos sendo empilhados na pia,
    usando os personagens das Tartarugas Ninja.
    """
    # Limpa a pilha atual
    pilha.clear()
    
    # Simula a ordem em que os personagens terminaram de comer
    # e colocaram seus pratos na pilha (primeiro a colocar fica embaixo)
    pilha.push('Prato do Splinter')      # Primeiro a terminar (base)
    pilha.push('Prato do Leonardo')      # Segundo a terminar
    pilha.push('Prato do Donatello')     # Terceiro a terminar
    pilha.push('Prato do Raphael')       # Quarto a terminar
    pilha.push('Prato do Michelangelo')  # Último a terminar (topo)
    
    print("\n🍕 Dados de exemplo carregados com sucesso!")
    print("Simulação: Pilha de pratos após jantar de pizza!")
    print("(Michelangelo sempre termina por último...)")


def demonstrar_lifo(pilha):
    """Demonstra o princípio LIFO da pilha"""
    print("\n" + "=" * 50)
    print("     DEMONSTRAÇÃO DO PRINCÍPIO LIFO")
    print("=" * 50)
    
    # Limpa e prepara a pilha
    pilha.clear()
    
    print("\n📥 Empilhando elementos na ordem:")
    elementos = ['Primeiro', 'Segundo', 'Terceiro']
    
    for elem in elementos:
        print(f"   push('{elem}')")
        pilha.push(elem)
    
    print("\n📤 Desempilhando elementos:")
    while not pilha.is_empty():
        elem = pilha.pop()
        print(f"   pop() -> '{elem}'")
    
    print("\n✅ Observe: a ordem de saída é inversa à de entrada!")
    print("   Isso é o princípio LIFO (Last In, First Out)")


def main():
    """Função principal com menu interativo"""
    # Cria uma nova pilha vazia
    pilha = Stack()
    
    print("\n🐢 Bem-vindo ao Gerenciador de Pilha!")
    print("Uma pilha funciona como uma pilha de pratos:")
    print("você só pode adicionar ou remover do TOPO.")
    
    # Loop principal do menu
    while True:
        # Exibe as opções disponíveis
        exibir_menu()
        
        # Captura a opção do usuário com tratamento de interrupção
        try:
            opcao = input("\nEscolha uma opção: ").strip()
        except KeyboardInterrupt:
            print("\n\nPrograma encerrado pelo usuário.")
            break
        
        # ===== Opção 0: Sair do programa =====
        if opcao == '0':
            print("\nObrigado por usar o Gerenciador de Pilha!")
            print("Cowabunga! 🐢")
            break
        
        # ===== Opção 1: Empilhar (push) =====
        elif opcao == '1':
            dado = input("Digite o valor a empilhar: ").strip()
            if dado:
                pilha.push(dado)
                print(f"'{dado}' empilhado com sucesso!")
                pilha.display()
            else:
                print("Erro: Valor não pode ser vazio.")
        
        # ===== Opção 2: Desempilhar (pop) =====
        elif opcao == '2':
            removido = pilha.pop()
            if removido is not None:
                print(f"'{removido}' desempilhado com sucesso!")
                if not pilha.is_empty():
                    pilha.display()
                else:
                    print("A pilha agora está vazia.")
        
        # ===== Opção 3: Visualizar topo (peek) =====
        elif opcao == '3':
            topo = pilha.peek()
            if topo is not None:
                print(f"Elemento no topo: '{topo}'")
        
        # ===== Opção 4: Exibir pilha completa =====
        elif opcao == '4':
            print("\n--- Estado atual da pilha ---")
            pilha.display()
            if not pilha.is_empty():
                print(f"\nElementos (topo → base): {pilha.to_list()}")
        
        # ===== Opção 5: Exibir tamanho da pilha =====
        elif opcao == '5':
            tamanho = pilha.size()
            print(f"A pilha possui {tamanho} elemento(s).")
        
        # ===== Opção 6: Verificar se está vazia =====
        elif opcao == '6':
            if pilha.is_empty():
                print("✓ A pilha está VAZIA.")
            else:
                print(f"✗ A pilha NÃO está vazia. Possui {pilha.size()} elemento(s).")
        
        # ===== Opção 7: Limpar pilha =====
        elif opcao == '7':
            if pilha.is_empty():
                print("A pilha já está vazia.")
            else:
                confirma = input("Tem certeza que deseja limpar a pilha? (s/n): ").strip().lower()
                if confirma == 's':
                    pilha.clear()
                    print("Pilha limpa com sucesso!")
                else:
                    print("Operação cancelada.")
        
        # ===== Opção 8: Carregar dados de exemplo =====
        elif opcao == '8':
            carregar_exemplo(pilha)
            pilha.display()
        
        # ===== Opção 9 (easter egg): Demonstrar LIFO =====
        elif opcao == '9':
            demonstrar_lifo(pilha)
        
        # ===== Opção inválida =====
        else:
            print("Opção inválida! Por favor, escolha uma opção de 0 a 8.")


# Ponto de entrada do programa
# Só executa a main() se o arquivo for executado diretamente
if __name__ == "__main__":
    main()