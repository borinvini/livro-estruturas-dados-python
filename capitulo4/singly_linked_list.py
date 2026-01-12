class Node:
    def __init__(self, dado=None):
        self.dado = dado  # Armazena o dado do nodo
        self.next = None  # Referência para o próximo nodo


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Inicialmente, a lista está vazia

    # ==================== MÉTODOS DE INSERÇÃO ====================

    def prepend(self, dado):
        """Insere um novo nodo no início da lista"""
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)
        
        # O próximo do novo nodo aponta para o antigo head
        novo_nodo.next = self.head
        
        # O head agora aponta para o novo nodo
        self.head = novo_nodo

    def append(self, dado):
        """Insere um novo nodo no final da lista"""
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)
        
        # Caso especial: lista vazia
        if self.head is None:
            self.head = novo_nodo
        else:
            # Percorre até o último nodo
            nodo_atual = self.head
            while nodo_atual.next:
                nodo_atual = nodo_atual.next
            
            # Conecta o último nodo ao novo nodo
            nodo_atual.next = novo_nodo

    def insert_at(self, dado, index):
        """Insere um novo nodo em uma posição específica da lista"""
        # Caso especial: inserção no início
        if index == 0:
            self.prepend(dado)
            return True
        
        # Cria o novo nodo
        novo_nodo = Node(dado)
        
        # Variáveis para percorrer a lista
        nodo_atual = self.head
        nodo_anterior = None
        posicao = 0
        
        # Percorre até a posição desejada
        while nodo_atual and posicao < index:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.next
            posicao += 1
        
        # Verifica se a posição existe
        if posicao < index:
            print(f"Erro: A lista tem apenas {posicao} elementos")
            return False
        
        # Conecta o novo nodo na posição correta
        # O novo nodo aponta para o nodo que estava na posição
        novo_nodo.next = nodo_atual
        
        # O nodo anterior agora aponta para o novo nodo
        nodo_anterior.next = novo_nodo
        return True

    # ==================== MÉTODOS DE REMOÇÃO ====================

    def remove_first(self):
        """Remove o primeiro nodo da lista (head)"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return None
        
        # Guarda o dado do nodo removido para retornar
        dado_removido = self.head.dado
        
        # O head passa a apontar para o segundo nodo
        # O antigo primeiro nodo será coletado pelo garbage collector
        self.head = self.head.next
        
        return dado_removido

    def remove_last(self):
        """Remove o último nodo da lista"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return None
        
        # Caso especial: lista com apenas um elemento
        # Neste caso, o head é também o último elemento
        if self.head.next is None:
            dado_removido = self.head.dado
            self.head = None
            return dado_removido
        
        # Percorre até o penúltimo nodo
        # Precisamos parar no penúltimo para poder desconectar o último
        nodo_atual = self.head
        while nodo_atual.next.next:
            nodo_atual = nodo_atual.next
        
        # Guarda o dado do último nodo antes de removê-lo
        dado_removido = nodo_atual.next.dado
        
        # O penúltimo nodo agora aponta para None
        # Isso "desconecta" o último nodo da lista
        nodo_atual.next = None
        
        return dado_removido

    def remove_at(self, index):
        """Remove o nodo em uma posição específica"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return None
        
        # Caso especial: remoção do primeiro elemento
        # Reutiliza o método remove_first() para evitar duplicação de código
        if index == 0:
            return self.remove_first()
        
        # Variáveis para percorrer a lista
        nodo_atual = self.head
        nodo_anterior = None
        posicao = 0
        
        # Percorre até a posição desejada
        # Mantemos referência ao nodo anterior para reconectar a lista
        while nodo_atual and posicao < index:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.next
            posicao += 1
        
        # Verifica se a posição existe
        # Se nodo_atual é None, significa que o índice está fora dos limites
        if nodo_atual is None:
            print(f"Erro: Índice {index} fora dos limites da lista")
            return None
        
        # Guarda o dado do nodo removido
        dado_removido = nodo_atual.dado
        
        # O nodo anterior agora aponta para o próximo do removido
        # Isso "pula" o nodo que queremos remover
        nodo_anterior.next = nodo_atual.next
        
        return dado_removido

    def remove(self, dado):
        """Remove a primeira ocorrência de um dado específico"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return False
        
        # Caso especial: o dado está no head
        # Precisamos tratar separadamente pois não há nodo anterior
        if self.head.dado == dado:
            self.head = self.head.next
            return True
        
        # Variáveis para percorrer a lista
        nodo_atual = self.head
        nodo_anterior = None
        
        # Percorre a lista procurando o dado
        # Continua enquanto houver nodos E o dado não for encontrado
        while nodo_atual and nodo_atual.dado != dado:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.next
        
        # Verifica se encontrou o dado
        # Se nodo_atual é None, percorreu toda a lista sem encontrar
        if nodo_atual is None:
            print(f"Erro: '{dado}' não encontrado na lista")
            return False
        
        # Remove o nodo reconectando os ponteiros
        # O anterior agora aponta para o próximo do nodo encontrado
        nodo_anterior.next = nodo_atual.next
        return True

    # ==================== MÉTODOS AUXILIARES ====================

    def traversal(self):
        """Percorre e exibe todos os elementos da lista"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return
        
        # Inicia a varredura a partir do head
        nodo_atual = self.head
        elementos = []
        index = 0
        
        # Percorre toda a lista até o final (quando next é None)
        while nodo_atual:
            # Formata cada elemento com seu índice
            elementos.append(f"[{index}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.next
            index += 1
        
        # Exibe os elementos separados por setas
        print(" -> ".join(elementos))
    
    def is_empty(self):
        """Verifica se a lista está vazia"""
        # A lista está vazia quando o head não aponta para nenhum nodo
        return self.head is None
    
    def size(self):
        """Retorna o tamanho da lista"""
        # Inicializa o contador
        contador = 0
        nodo_atual = self.head
        
        # Percorre toda a lista contando os nodos
        while nodo_atual:
            contador += 1
            nodo_atual = nodo_atual.next
        
        return contador


# ==================== FUNÇÕES DO MENU ====================

def exibir_menu():
    """Exibe o menu de opções para o usuário"""
    print("\n" + "=" * 50)
    print("       GERENCIADOR DE LISTA ENCADEADA")
    print("=" * 50)
    print("\n--- INSERÇÃO ---")
    print("1. Inserir no início (prepend)")
    print("2. Inserir no final (append)")
    print("3. Inserir em posição específica (insert_at)")
    print("\n--- REMOÇÃO ---")
    print("4. Remover do início (remove_first)")
    print("5. Remover do final (remove_last)")
    print("6. Remover de posição específica (remove_at)")
    print("7. Remover por valor (remove)")
    print("\n--- VISUALIZAÇÃO ---")
    print("8. Exibir lista completa")
    print("9. Exibir tamanho da lista")
    print("\n--- SISTEMA ---")
    print("10. Carregar dados de exemplo")
    print("0. Sair")
    print("=" * 50)


def carregar_exemplo(lista):
    """Carrega dados de exemplo na lista para demonstração"""
    # Limpa a lista atual removendo a referência ao head
    lista.head = None
    
    # Insere os personagens das Tartarugas Ninja
    lista.append('Leonardo')      # O líder, usa espadas katana
    lista.append('Raphael')       # O valentão, usa sais
    lista.append('Donatello')     # O gênio, usa bastão bo
    lista.append('Michelangelo')  # O engraçado, usa nunchakus
    lista.prepend('Splinter')     # O mestre, inserido no início
    lista.append('April')         # A amiga jornalista
    
    print("Dados de exemplo carregados com sucesso!")
    print("Personagens das Tartarugas Ninja inseridos.")


def main():
    """Função principal com menu interativo"""
    # Cria uma nova lista encadeada vazia
    lista = SinglyLinkedList()
    
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
            print("\nObrigado por usar o Gerenciador de Lista Encadeada!")
            print("Cowabunga! 🐢")
            break
        
        # ===== Opção 1: Inserir no início (prepend) =====
        elif opcao == '1':
            dado = input("Digite o valor a inserir no início: ").strip()
            if dado:
                lista.prepend(dado)
                print(f"'{dado}' inserido no início com sucesso!")
                lista.traversal()
            else:
                print("Erro: Valor não pode ser vazio.")
        
        # ===== Opção 2: Inserir no final (append) =====
        elif opcao == '2':
            dado = input("Digite o valor a inserir no final: ").strip()
            if dado:
                lista.append(dado)
                print(f"'{dado}' inserido no final com sucesso!")
                lista.traversal()
            else:
                print("Erro: Valor não pode ser vazio.")
        
        # ===== Opção 3: Inserir em posição específica (insert_at) =====
        elif opcao == '3':
            dado = input("Digite o valor a inserir: ").strip()
            if not dado:
                print("Erro: Valor não pode ser vazio.")
                continue
            try:
                index = int(input("Digite a posição (índice): "))
                if index < 0:
                    print("Erro: O índice deve ser um número positivo.")
                    continue
                if lista.insert_at(dado, index):
                    print(f"'{dado}' inserido na posição {index} com sucesso!")
                    lista.traversal()
            except ValueError:
                print("Erro: Digite um número inteiro válido.")
        
        # ===== Opção 4: Remover do início (remove_first) =====
        elif opcao == '4':
            removido = lista.remove_first()
            if removido is not None:
                print(f"'{removido}' removido do início com sucesso!")
                lista.traversal()
        
        # ===== Opção 5: Remover do final (remove_last) =====
        elif opcao == '5':
            removido = lista.remove_last()
            if removido is not None:
                print(f"'{removido}' removido do final com sucesso!")
                lista.traversal()
        
        # ===== Opção 6: Remover de posição específica (remove_at) =====
        elif opcao == '6':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            try:
                index = int(input("Digite a posição a remover (índice): "))
                if index < 0:
                    print("Erro: O índice deve ser um número positivo.")
                    continue
                removido = lista.remove_at(index)
                if removido is not None:
                    print(f"'{removido}' removido da posição {index} com sucesso!")
                    lista.traversal()
            except ValueError:
                print("Erro: Digite um número inteiro válido.")
        
        # ===== Opção 7: Remover por valor (remove) =====
        elif opcao == '7':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            dado = input("Digite o valor a remover: ").strip()
            if lista.remove(dado):
                print(f"'{dado}' removido com sucesso!")
                lista.traversal()
        
        # ===== Opção 8: Exibir lista completa =====
        elif opcao == '8':
            print("\n--- Estado atual da lista ---")
            lista.traversal()
        
        # ===== Opção 9: Exibir tamanho da lista =====
        elif opcao == '9':
            tamanho = lista.size()
            print(f"A lista possui {tamanho} elemento(s).")
        
        # ===== Opção 10: Carregar dados de exemplo =====
        elif opcao == '10':
            carregar_exemplo(lista)
            lista.traversal()
        
        # ===== Opção inválida =====
        else:
            print("Opção inválida! Por favor, escolha uma opção de 0 a 10.")


# Ponto de entrada do programa
# Só executa a main() se o arquivo for executado diretamente
if __name__ == "__main__":
    main()