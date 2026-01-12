class Node:
    def __init__(self, dado=None):
        self.dado = dado  # Armazena o dado do nodo
        self.next = None  # Referência para o próximo nodo


class Queue:
    """
    Implementação de Fila (Queue) usando Lista Encadeada.
    
    A fila segue o princípio FIFO (First In, First Out):
    o primeiro elemento inserido é o primeiro a ser removido.
    
    Mantém referências para o início (inicio) e o final (fim) da fila,
    garantindo operações O(1) para enqueue e dequeue.
    """
    
    def __init__(self):
        self.inicio = None  # Referência para o início da fila (onde sai)
        self.fim = None     # Referência para o final da fila (onde entra)
        self._size = 0      # Contador de elementos para acesso O(1) ao tamanho

    # ==================== OPERAÇÕES PRINCIPAIS ====================

    def enqueue(self, dado):
        """
        Insere um novo elemento no final da fila.
        
        Complexidade: O(1)
        
        Args:
            dado: O valor a ser inserido na fila
        """
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)
        
        # Caso especial: fila vazia
        # Tanto inicio quanto fim apontam para o novo nodo
        if self.fim is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            # O último nodo agora aponta para o novo nodo
            self.fim.next = novo_nodo
            # Fim passa a apontar para o novo nodo
            self.fim = novo_nodo
        
        # Incrementa o contador de elementos
        self._size += 1

    def dequeue(self):
        """
        Remove e retorna o elemento do início da fila.
        
        Complexidade: O(1)
        
        Returns:
            O dado do elemento removido, ou None se a fila estiver vazia
        
        Raises:
            Exibe mensagem de erro se a fila estiver vazia
        """
        # Caso especial: fila vazia
        if self.inicio is None:
            print("Erro: A fila está vazia (Queue Underflow)")
            return None
        
        # Guarda o dado do nodo removido para retornar
        dado_removido = self.inicio.dado
        
        # Inicio passa a apontar para o próximo nodo
        self.inicio = self.inicio.next
        
        # Caso especial: a fila ficou vazia após a remoção
        # Precisamos atualizar fim também para None
        if self.inicio is None:
            self.fim = None
        
        # Decrementa o contador de elementos
        self._size -= 1
        
        return dado_removido

    def peek(self):
        """
        Retorna o elemento do início da fila sem removê-lo.
        
        Também conhecido como front() em algumas implementações.
        
        Complexidade: O(1)
        
        Returns:
            O dado do elemento no início, ou None se a fila estiver vazia
        """
        # Caso especial: fila vazia
        if self.inicio is None:
            print("Erro: A fila está vazia")
            return None
        
        # Retorna o dado do início sem modificar a fila
        return self.inicio.dado

    def peek_fim(self):
        """
        Retorna o elemento do final da fila sem removê-lo.
        
        Complexidade: O(1)
        
        Returns:
            O dado do elemento no final, ou None se a fila estiver vazia
        """
        # Caso especial: fila vazia
        if self.fim is None:
            print("Erro: A fila está vazia")
            return None
        
        # Retorna o dado do final sem modificar a fila
        return self.fim.dado

    # ==================== MÉTODOS AUXILIARES ====================

    def is_empty(self):
        """
        Verifica se a fila está vazia.
        
        Complexidade: O(1)
        
        Returns:
            True se a fila estiver vazia, False caso contrário
        """
        return self.inicio is None

    def size(self):
        """
        Retorna o número de elementos na fila.
        
        Complexidade: O(1) - usa contador interno
        
        Returns:
            Número de elementos na fila
        """
        return self._size

    def clear(self):
        """
        Remove todos os elementos da fila.
        
        Complexidade: O(1)
        """
        self.inicio = None
        self.fim = None
        self._size = 0

    def display(self):
        """
        Exibe todos os elementos da fila, do início ao final.
        
        Complexidade: O(n)
        """
        # Caso especial: fila vazia
        if self.inicio is None:
            print("Fila vazia")
            return
        
        print("\n    SAÍDA                                    ENTRADA")
        print("    (inicio)                                   (fim)")
        print("      ↓                                         ↓")
        
        # Constrói a representação visual da fila
        nodo_atual = self.inicio
        posicao = 0
        elementos = []
        
        while nodo_atual:
            elementos.append(f"[{posicao}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.next
            posicao += 1
        
        # Exibe os elementos em formato horizontal
        linha_superior = "    ┌" + "─" * 15 + "┐"
        linha_inferior = "    └" + "─" * 15 + "┘"
        
        for i, elem in enumerate(elementos):
            print(linha_superior)
            print(f"    │ {elem:^13} │", end="")
            if i == 0:
                print(" ← PRÓXIMO A SAIR", end="")
            elif i == len(elementos) - 1:
                print(" ← ÚLTIMO A ENTRAR", end="")
            print()
            print(linha_inferior)
            if i < len(elementos) - 1:
                print("           ↓")

    def display_horizontal(self):
        """
        Exibe a fila em formato horizontal compacto.
        
        Complexidade: O(n)
        """
        if self.inicio is None:
            print("Fila vazia")
            return
        
        nodo_atual = self.inicio
        elementos = []
        index = 0
        
        while nodo_atual:
            elementos.append(f"[{index}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.next
            index += 1
        
        print("\n  INÍCIO                                     FIM")
        print("  (saída)                                (entrada)")
        print("    ↓                                        ↓")
        print("    " + " → ".join(elementos))

    def to_list(self):
        """
        Converte a fila em uma lista Python (do inicio ao fim).
        
        Complexidade: O(n)
        
        Returns:
            Lista com os elementos da fila
        """
        elementos = []
        nodo_atual = self.inicio
        
        while nodo_atual:
            elementos.append(nodo_atual.dado)
            nodo_atual = nodo_atual.next
        
        return elementos


# ==================== FUNÇÕES DO MENU ====================

def exibir_menu():
    """Exibe o menu de opções para o usuário"""
    print("\n" + "=" * 50)
    print("          GERENCIADOR DE FILA (QUEUE)")
    print("            Implementação com Lista")
    print("=" * 50)
    print("\n--- OPERAÇÕES PRINCIPAIS ---")
    print("1. Inserir na fila (enqueue)")
    print("2. Remover da fila (dequeue)")
    print("3. Visualizar início (peek)")
    print("4. Visualizar final (peek_fim)")
    print("\n--- VISUALIZAÇÃO ---")
    print("5. Exibir fila completa (vertical)")
    print("6. Exibir fila compacta (horizontal)")
    print("7. Exibir tamanho da fila")
    print("8. Verificar se está vazia")
    print("\n--- SISTEMA ---")
    print("9. Limpar fila")
    print("10. Carregar dados de exemplo")
    print("0. Sair")
    print("=" * 50)


def carregar_exemplo(fila):
    """
    Carrega dados de exemplo na fila para demonstração.
    
    Simula uma fila de atendimento na pizzaria das Tartarugas Ninja.
    Quem chegou primeiro será atendido primeiro (FIFO).
    """
    # Limpa a fila atual
    fila.clear()
    
    # Simula a ordem de chegada na pizzaria
    # Primeiro a chegar será o primeiro a ser atendido
    fila.enqueue('Leonardo')      # Chegou primeiro (inicio)
    fila.enqueue('Donatello')     # Chegou segundo
    fila.enqueue('Raphael')       # Chegou terceiro
    fila.enqueue('Michelangelo')  # Chegou quarto
    fila.enqueue('April')         # Chegou quinta
    fila.enqueue('Splinter')      # Chegou por último (fim)
    
    print("\n🍕 Dados de exemplo carregados com sucesso!")
    print("Simulação: Fila de atendimento na pizzaria!")
    print("(Leonardo chegou primeiro e será atendido primeiro)")


def demonstrar_fifo(fila):
    """Demonstra o princípio FIFO da fila"""
    print("\n" + "=" * 50)
    print("     DEMONSTRAÇÃO DO PRINCÍPIO FIFO")
    print("=" * 50)
    
    # Limpa e prepara a fila
    fila.clear()
    
    print("\n📥 Inserindo elementos na fila (enqueue):")
    elementos = ['Primeiro', 'Segundo', 'Terceiro']
    
    for elem in elementos:
        print(f"   enqueue('{elem}')")
        fila.enqueue(elem)
    
    print("\n📤 Removendo elementos da fila (dequeue):")
    while not fila.is_empty():
        elem = fila.dequeue()
        print(f"   dequeue() -> '{elem}'")
    
    print("\n✅ Observe: a ordem de saída é IGUAL à de entrada!")
    print("   Isso é o princípio FIFO (First In, First Out)")


def main():
    """Função principal com menu interativo"""
    # Cria uma nova fila vazia
    fila = Queue()
    
    print("\n🐢 Bem-vindo ao Gerenciador de Fila!")
    print("Uma fila funciona como uma fila de banco:")
    print("quem chega primeiro é atendido primeiro.")
    
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
            print("\nObrigado por usar o Gerenciador de Fila!")
            print("Cowabunga! 🐢")
            break
        
        # ===== Opção 1: Inserir na fila (enqueue) =====
        elif opcao == '1':
            dado = input("Digite o valor a inserir na fila: ").strip()
            if dado:
                fila.enqueue(dado)
                print(f"'{dado}' entrou na fila com sucesso!")
                fila.display_horizontal()
            else:
                print("Erro: Valor não pode ser vazio.")
        
        # ===== Opção 2: Remover da fila (dequeue) =====
        elif opcao == '2':
            removido = fila.dequeue()
            if removido is not None:
                print(f"'{removido}' saiu da fila com sucesso!")
                if not fila.is_empty():
                    fila.display_horizontal()
                else:
                    print("A fila agora está vazia.")
        
        # ===== Opção 3: Visualizar início (peek) =====
        elif opcao == '3':
            inicio = fila.peek()
            if inicio is not None:
                print(f"Próximo a ser atendido (inicio): '{inicio}'")
        
        # ===== Opção 4: Visualizar final (peek_fim) =====
        elif opcao == '4':
            final = fila.peek_fim()
            if final is not None:
                print(f"Último da fila (fim): '{final}'")
        
        # ===== Opção 5: Exibir fila completa (vertical) =====
        elif opcao == '5':
            print("\n--- Estado atual da fila ---")
            fila.display()
        
        # ===== Opção 6: Exibir fila compacta (horizontal) =====
        elif opcao == '6':
            print("\n--- Estado atual da fila ---")
            fila.display_horizontal()
            if not fila.is_empty():
                print(f"\nElementos: {fila.to_list()}")
        
        # ===== Opção 7: Exibir tamanho da fila =====
        elif opcao == '7':
            tamanho = fila.size()
            print(f"A fila possui {tamanho} elemento(s).")
        
        # ===== Opção 8: Verificar se está vazia =====
        elif opcao == '8':
            if fila.is_empty():
                print("✓ A fila está VAZIA.")
            else:
                print(f"✗ A fila NÃO está vazia. Possui {fila.size()} elemento(s).")
        
        # ===== Opção 9: Limpar fila =====
        elif opcao == '9':
            if fila.is_empty():
                print("A fila já está vazia.")
            else:
                confirma = input("Tem certeza que deseja limpar a fila? (s/n): ").strip().lower()
                if confirma == 's':
                    fila.clear()
                    print("Fila limpa com sucesso!")
                else:
                    print("Operação cancelada.")
        
        # ===== Opção 10: Carregar dados de exemplo =====
        elif opcao == '10':
            carregar_exemplo(fila)
            fila.display_horizontal()
        
        # ===== Opção 11 (easter egg): Demonstrar FIFO =====
        elif opcao == '11':
            demonstrar_fifo(fila)
        
        # ===== Opção inválida =====
        else:
            print("Opção inválida! Por favor, escolha uma opção de 0 a 10.")


# Ponto de entrada do programa
# Só executa a main() se o arquivo for executado diretamente
if __name__ == "__main__":
    main()