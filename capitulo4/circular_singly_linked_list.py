class Node:
    def __init__(self, dado=None):
        self.dado = dado  # Armazena o dado do nodo
        self.next = None  # Referência para o próximo nodo


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Referência para o primeiro nodo
        self.tail = None  # Referência para o último nodo (aponta de volta ao head)

    # ==================== MÉTODOS DE INSERÇÃO ====================

    def prepend(self, dado):
        """Insere um novo nodo no início da lista"""
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)

        # Caso especial: lista vazia
        # Quando a lista está vazia, o nodo aponta para si mesmo
        if self.head is None:
            self.head = novo_nodo
            self.tail = novo_nodo
            novo_nodo.next = novo_nodo  # Aponta para si mesmo (circular)
        else:
            # O próximo do novo nodo aponta para o antigo head
            novo_nodo.next = self.head

            # O tail continua apontando para o novo head (mantém a circularidade)
            self.tail.next = novo_nodo

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
            novo_nodo.next = novo_nodo  # Aponta para si mesmo (circular)
        else:
            # O próximo do novo nodo aponta para o head (mantém a circularidade)
            novo_nodo.next = self.head

            # O antigo tail agora aponta para o novo nodo
            self.tail.next = novo_nodo

            # O tail agora é o novo nodo
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
        nodo_anterior = None
        posicao = 0

        # Percorre até a posição desejada
        # Na lista circular, precisamos verificar se voltamos ao head
        while posicao < index:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.next

            # Se voltou ao head, chegamos ao "fim" da lista
            if nodo_atual == self.head:
                break

            posicao += 1

        # Verifica se a posição existe
        if posicao < index - 1:
            print(f"Erro: A lista tem apenas {posicao + 1} elementos")
            return False

        # Caso especial: inserção no final (após o tail)
        if nodo_atual == self.head and posicao == index - 1:
            self.append(dado)
            return True

        # Conecta o novo nodo na posição correta
        novo_nodo.next = nodo_atual
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

        # Caso especial: lista com apenas um elemento
        # Quando head e tail são o mesmo nodo
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # O head passa a apontar para o segundo nodo
            self.head = self.head.next

            # O tail agora aponta para o novo head (mantém a circularidade)
            self.tail.next = self.head

        return dado_removido

    def remove_last(self):
        """Remove o último nodo da lista (tail)"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return None

        # Guarda o dado do nodo removido para retornar
        dado_removido = self.tail.dado

        # Caso especial: lista com apenas um elemento
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Percorre até o penúltimo nodo
            # Na lista circular simples, precisamos percorrer toda a lista
            nodo_atual = self.head
            while nodo_atual.next != self.tail:
                nodo_atual = nodo_atual.next

            # O penúltimo nodo agora é o novo tail
            self.tail = nodo_atual

            # O novo tail aponta para o head (mantém a circularidade)
            self.tail.next = self.head

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
        nodo_anterior = None
        posicao = 0

        # Percorre até a posição desejada
        while posicao < index:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.next

            # Se voltou ao head, o índice está fora dos limites
            if nodo_atual == self.head:
                print(f"Erro: Índice {index} fora dos limites da lista")
                return None

            posicao += 1

        # Guarda o dado do nodo removido
        dado_removido = nodo_atual.dado

        # Caso especial: remoção do último elemento (tail)
        if nodo_atual == self.tail:
            return self.remove_last()

        # Reconecta os nodos, "pulando" o nodo removido
        nodo_anterior.next = nodo_atual.next

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
        nodo_atual = self.head.next  # Começa do segundo nodo
        nodo_anterior = self.head

        # Continua enquanto não voltar ao head
        while nodo_atual != self.head:
            if nodo_atual.dado == dado:
                # Reconecta os nodos
                nodo_anterior.next = nodo_atual.next
                return True

            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.next

        print(f"Erro: '{dado}' não encontrado na lista")
        return False

    # ==================== MÉTODOS DE BUSCA ====================

    def search(self, dado):
        """Busca um dado na lista e retorna sua posição (ou -1 se não encontrado)"""
        # Caso especial: lista vazia
        if self.head is None:
            return -1

        # Verifica se está no head
        if self.head.dado == dado:
            return 0

        # Percorre a lista procurando o dado
        nodo_atual = self.head.next
        posicao = 1

        # Continua enquanto não voltar ao head
        while nodo_atual != self.head:
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

        # Caso especial: índice negativo
        if index < 0:
            print("Erro: O índice deve ser um número positivo")
            return None

        # Percorre até a posição desejada
        nodo_atual = self.head
        posicao = 0

        while posicao < index:
            nodo_atual = nodo_atual.next

            # Se voltou ao head, o índice está fora dos limites
            if nodo_atual == self.head:
                print(f"Erro: Índice {index} fora dos limites da lista")
                return None

            posicao += 1

        return nodo_atual.dado

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

        # Percorre toda a lista usando do-while (executa pelo menos uma vez)
        while True:
            elementos.append(f"[{index}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.next
            index += 1

            # Para quando voltar ao head (completou o ciclo)
            if nodo_atual == self.head:
                break

        # Exibe os elementos com seta circular no final
        print(" -> ".join(elementos) + " -> (volta ao início)")

    def traversal_n_vezes(self, voltas=2):
        """Percorre a lista N vezes para demonstrar a circularidade"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return

        # Calcula quantos elementos exibir
        tamanho = self.size()
        total_elementos = tamanho * voltas

        nodo_atual = self.head
        elementos = []

        for i in range(total_elementos):
            # Marca quando completa uma volta
            if i > 0 and i % tamanho == 0:
                elementos.append("| VOLTA |")
            elementos.append(nodo_atual.dado)
            nodo_atual = nodo_atual.next

        print(" -> ".join(elementos))

    def is_empty(self):
        """Verifica se a lista está vazia"""
        return self.head is None

    def size(self):
        """Retorna o tamanho da lista"""
        # Caso especial: lista vazia
        if self.head is None:
            return 0

        # Conta os elementos
        contador = 1  # Começa em 1 pois já conta o head
        nodo_atual = self.head.next

        # Continua enquanto não voltar ao head
        while nodo_atual != self.head:
            contador += 1
            nodo_atual = nodo_atual.next

        return contador


# ==================== FUNÇÕES DO MENU ====================

def exibir_menu():
    """Exibe o menu de opções para o usuário"""
    print("\n" + "=" * 58)
    print("     GERENCIADOR DE LISTA CIRCULAR SIMPLESMENTE ENCADEADA")
    print("=" * 58)
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
    print("10. Exibir lista")
    print("11. Demonstrar circularidade (N voltas)")
    print("12. Exibir tamanho da lista")
    print("\n--- SISTEMA ---")
    print("13. Carregar dados de exemplo")
    print("0. Sair")
    print("=" * 58)


def carregar_exemplo(lista):
    """Carrega dados de exemplo na lista para demonstração"""
    # Limpa a lista atual
    lista.head = None
    lista.tail = None

    # Insere os personagens das Tartarugas Ninja
    # Imagine uma roda de treinamento onde cada um passa a vez para o próximo!
    lista.append('Leonardo')      # O líder, usa espadas katana
    lista.append('Raphael')       # O valentão, usa sais
    lista.append('Donatello')     # O gênio, usa bastão bo
    lista.append('Michelangelo')  # O engraçado, usa nunchakus

    print("Dados de exemplo carregados com sucesso!")
    print("Tartarugas Ninja em formação circular de treinamento!")


def main():
    """Função principal com menu interativo"""
    # Cria uma nova lista circular simplesmente encadeada vazia
    lista = CircularLinkedList()

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
            print("\nObrigado por usar o Gerenciador de Lista Circular!")
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

        # ===== Opção 10: Exibir lista =====
        elif opcao == '10':
            print("\n--- Estado atual da lista circular ---")
            lista.traversal()

        # ===== Opção 11: Demonstrar circularidade =====
        elif opcao == '11':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            try:
                voltas = int(input("Quantas voltas deseja visualizar? (1-5): "))
                if voltas < 1 or voltas > 5:
                    print("Erro: Digite um número entre 1 e 5.")
                    continue
                print(f"\n--- Demonstrando {voltas} volta(s) na lista circular ---")
                lista.traversal_n_vezes(voltas)
            except ValueError:
                print("Erro: Digite um número inteiro válido.")

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