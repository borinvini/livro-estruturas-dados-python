class Node:
    def __init__(self, dado=None):
        self.dado = dado  # Armazena o dado do nodo
        self.next = None  # Referência para o próximo nodo
        self.prev = None  # Referência para o nodo anterior


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Referência para o primeiro nodo
        self.tail = None  # Referência para o último nodo

    # ==================== MÉTODOS DE INSERÇÃO ====================

    def prepend(self, dado):
        """Insere um novo nodo no início da lista"""
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)

        # Caso especial: lista vazia
        # Quando a lista está vazia, o novo nodo será tanto o head quanto o tail
        if self.head is None:
            self.head = novo_nodo
            self.tail = novo_nodo
        else:
            # O próximo do novo nodo aponta para o antigo head
            novo_nodo.next = self.head

            # O anterior do antigo head aponta para o novo nodo
            # Esta é a diferença da lista simples: precisamos atualizar o prev
            self.head.prev = novo_nodo

            # O head agora aponta para o novo nodo
            self.head = novo_nodo

    def append(self, dado):
        """Insere um novo nodo no final da lista"""
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)

        # Caso especial: lista vazia
        if self.head is None:
            self.head = novo_nodo
            self.tail = novo_nodo
        else:
            # O anterior do novo nodo aponta para o antigo tail
            novo_nodo.prev = self.tail

            # O próximo do antigo tail aponta para o novo nodo
            self.tail.next = novo_nodo

            # O tail agora aponta para o novo nodo
            # Vantagem da lista dupla: não precisamos percorrer toda a lista!
            self.tail = novo_nodo

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
        posicao = 0

        # Percorre até a posição desejada
        while nodo_atual and posicao < index:
            nodo_atual = nodo_atual.next
            posicao += 1

        # Verifica se a posição existe
        if posicao < index and nodo_atual is None:
            print(f"Erro: A lista tem apenas {posicao} elementos")
            return False

        # Caso especial: inserção no final (nodo_atual é None)
        if nodo_atual is None:
            self.append(dado)
            return True

        # Obtém o nodo anterior através do ponteiro prev
        # Vantagem da lista dupla: não precisamos manter variável nodo_anterior
        nodo_anterior = nodo_atual.prev

        # Conecta o novo nodo na posição correta
        # O novo nodo aponta para frente e para trás
        novo_nodo.next = nodo_atual
        novo_nodo.prev = nodo_anterior

        # Atualiza as referências dos nodos adjacentes
        # O anterior agora aponta para o novo nodo
        nodo_anterior.next = novo_nodo
        # O atual agora tem o novo nodo como anterior
        nodo_atual.prev = novo_nodo

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

        # Caso especial: lista com apenas um elemento
        # Neste caso, head e tail apontam para o mesmo nodo
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # O head passa a apontar para o segundo nodo
            self.head = self.head.next

            # O novo head não tem mais nodo anterior
            # Isso "desconecta" o antigo primeiro nodo
            self.head.prev = None

        return dado_removido

    def remove_last(self):
        """Remove o último nodo da lista (tail)"""
        # Caso especial: lista vazia
        if self.tail is None:
            print("Erro: A lista está vazia")
            return None

        # Guarda o dado do nodo removido para retornar
        dado_removido = self.tail.dado

        # Caso especial: lista com apenas um elemento
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # O tail passa a apontar para o penúltimo nodo
            # Vantagem da lista dupla: acesso direto via tail.prev!
            self.tail = self.tail.prev

            # O novo tail não tem mais próximo nodo
            # Isso "desconecta" o antigo último nodo
            self.tail.next = None

        return dado_removido

    def remove_at(self, index):
        """Remove o nodo em uma posição específica"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return None

        # Caso especial: remoção do primeiro elemento
        if index == 0:
            return self.remove_first()

        # Variáveis para percorrer a lista
        nodo_atual = self.head
        posicao = 0

        # Percorre até a posição desejada
        while nodo_atual and posicao < index:
            nodo_atual = nodo_atual.next
            posicao += 1

        # Verifica se a posição existe
        if nodo_atual is None:
            print(f"Erro: Índice {index} fora dos limites da lista")
            return None

        # Guarda o dado do nodo removido
        dado_removido = nodo_atual.dado

        # Caso especial: remoção do último elemento
        if nodo_atual == self.tail:
            return self.remove_last()

        # Obtém os nodos adjacentes através dos ponteiros
        nodo_anterior = nodo_atual.prev
        nodo_proximo = nodo_atual.next

        # Reconecta os nodos adjacentes, "pulando" o nodo removido
        # O anterior agora aponta para o próximo do removido
        nodo_anterior.next = nodo_proximo
        # O próximo agora tem o anterior do removido como seu anterior
        nodo_proximo.prev = nodo_anterior

        return dado_removido

    def remove(self, dado):
        """Remove a primeira ocorrência de um dado específico"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return False

        # Caso especial: o dado está no head
        if self.head.dado == dado:
            self.remove_first()
            return True

        # Caso especial: o dado está no tail
        if self.tail.dado == dado:
            self.remove_last()
            return True

        # Percorre a lista procurando o dado
        nodo_atual = self.head

        # Continua enquanto houver nodos E o dado não for encontrado
        while nodo_atual and nodo_atual.dado != dado:
            nodo_atual = nodo_atual.next

        # Verifica se encontrou o dado
        if nodo_atual is None:
            print(f"Erro: '{dado}' não encontrado na lista")
            return False

        # Obtém os nodos adjacentes
        nodo_anterior = nodo_atual.prev
        nodo_proximo = nodo_atual.next

        # Reconecta os nodos adjacentes
        nodo_anterior.next = nodo_proximo
        nodo_proximo.prev = nodo_anterior

        return True

    # ==================== MÉTODOS DE BUSCA ====================

    def search(self, dado):
        """Busca um dado na lista e retorna sua posição (ou -1 se não encontrado)"""
        # Caso especial: lista vazia
        if self.head is None:
            return -1

        # Percorre a lista procurando o dado
        nodo_atual = self.head
        posicao = 0

        while nodo_atual:
            if nodo_atual.dado == dado:
                return posicao
            nodo_atual = nodo_atual.next
            posicao += 1

        # Não encontrou o dado
        return -1

    def get(self, index):
        """Retorna o dado em uma posição específica"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return None

        # Otimização: decide se começa pelo head ou tail
        # Se o índice está na primeira metade, começa pelo head
        # Se está na segunda metade, começa pelo tail (mais eficiente!)
        tamanho = self.size()

        if index < 0 or index >= tamanho:
            print(f"Erro: Índice {index} fora dos limites da lista")
            return None

        # Decide a direção da busca
        if index <= tamanho // 2:
            # Busca a partir do head (início)
            nodo_atual = self.head
            for _ in range(index):
                nodo_atual = nodo_atual.next
        else:
            # Busca a partir do tail (fim) - vantagem da lista dupla!
            nodo_atual = self.tail
            for _ in range(tamanho - 1 - index):
                nodo_atual = nodo_atual.prev

        return nodo_atual.dado

    # ==================== MÉTODOS AUXILIARES ====================

    def traversal(self):
        """Percorre e exibe todos os elementos da lista (do início ao fim)"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return

        # Inicia a varredura a partir do head
        nodo_atual = self.head
        elementos = []
        index = 0

        # Percorre toda a lista até o final
        while nodo_atual:
            elementos.append(f"[{index}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.next
            index += 1

        # Exibe os elementos separados por setas bidirecionais
        print(" <-> ".join(elementos))

    def traversal_reverso(self):
        """Percorre e exibe todos os elementos da lista (do fim ao início)"""
        # Caso especial: lista vazia
        if self.tail is None:
            print("Lista vazia")
            return

        # Inicia a varredura a partir do tail
        nodo_atual = self.tail
        elementos = []
        index = self.size() - 1

        # Percorre toda a lista até o início usando o ponteiro prev
        while nodo_atual:
            elementos.append(f"[{index}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.prev
            index -= 1

        # Exibe os elementos separados por setas bidirecionais
        print(" <-> ".join(elementos))

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
    print("\n" + "=" * 55)
    print("     GERENCIADOR DE LISTA DUPLAMENTE ENCADEADA")
    print("=" * 55)
    print("\n--- INSERÇÃO ---")
    print("1. Inserir no início (prepend)")
    print("2. Inserir no final (append)")
    print("3. Inserir em posição específica (insert_at)")
    print("\n--- REMOÇÃO ---")
    print("4. Remover do início (remove_first)")
    print("5. Remover do final (remove_last)")
    print("6. Remover de posição específica (remove_at)")
    print("7. Remover por valor (remove)")
    print("\n--- BUSCA ---")
    print("8. Buscar elemento (search)")
    print("9. Obter elemento por índice (get)")
    print("\n--- VISUALIZAÇÃO ---")
    print("10. Exibir lista (head -> tail)")
    print("11. Exibir lista reversa (tail -> head)")
    print("12. Exibir tamanho da lista")
    print("\n--- SISTEMA ---")
    print("13. Carregar dados de exemplo")
    print("0. Sair")
    print("=" * 55)


def carregar_exemplo(lista):
    """Carrega dados de exemplo na lista para demonstração"""
    # Limpa a lista atual
    lista.head = None
    lista.tail = None

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
    # Cria uma nova lista duplamente encadeada vazia
    lista = DoublyLinkedList()

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
            print("\nObrigado por usar o Gerenciador de Lista Duplamente Encadeada!")
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

        # ===== Opção 8: Buscar elemento (search) =====
        elif opcao == '8':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            dado = input("Digite o valor a buscar: ").strip()
            posicao = lista.search(dado)
            if posicao >= 0:
                print(f"'{dado}' encontrado na posição {posicao}.")
            else:
                print(f"'{dado}' não encontrado na lista.")

        # ===== Opção 9: Obter elemento por índice (get) =====
        elif opcao == '9':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            try:
                index = int(input("Digite o índice do elemento: "))
                dado = lista.get(index)
                if dado is not None:
                    print(f"Elemento na posição {index}: '{dado}'")
            except ValueError:
                print("Erro: Digite um número inteiro válido.")

        # ===== Opção 10: Exibir lista (head -> tail) =====
        elif opcao == '10':
            print("\n--- Lista (head -> tail) ---")
            lista.traversal()

        # ===== Opção 11: Exibir lista reversa (tail -> head) =====
        elif opcao == '11':
            print("\n--- Lista reversa (tail -> head) ---")
            lista.traversal_reverso()

        # ===== Opção 12: Exibir tamanho da lista =====
        elif opcao == '12':
            tamanho = lista.size()
            print(f"A lista possui {tamanho} elemento(s).")

        # ===== Opção 13: Carregar dados de exemplo =====
        elif opcao == '13':
            carregar_exemplo(lista)
            lista.traversal()

        # ===== Opção inválida =====
        else:
            print("Opção inválida! Por favor, escolha uma opção de 0 a 13.")


# Ponto de entrada do programa
# Só executa a main() se o arquivo for executado diretamente
if __name__ == "__main__":
    main()