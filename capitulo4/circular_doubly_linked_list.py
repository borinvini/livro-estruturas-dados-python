class Node:
    def __init__(self, dado=None):
        self.dado = dado  # Armazena o dado do nodo
        self.next = None  # Referência para o próximo nodo
        self.prev = None  # Referência para o nodo anterior


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None  # Referência para o primeiro nodo
        self.tail = None  # Referência para o último nodo

    # ==================== MÉTODOS DE INSERÇÃO ====================

    def prepend(self, dado):
        """Insere um novo nodo no início da lista"""
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)

        # Caso especial: lista vazia
        # Quando a lista está vazia, o nodo aponta para si mesmo em ambas direções
        if self.head is None:
            self.head = novo_nodo
            self.tail = novo_nodo
            novo_nodo.next = novo_nodo  # Circular: aponta para si mesmo
            novo_nodo.prev = novo_nodo  # Circular: aponta para si mesmo
        else:
            # Conecta o novo nodo na estrutura circular
            # O próximo do novo nodo aponta para o antigo head
            novo_nodo.next = self.head

            # O anterior do novo nodo aponta para o tail (circularidade)
            novo_nodo.prev = self.tail

            # O anterior do antigo head agora é o novo nodo
            self.head.prev = novo_nodo

            # O próximo do tail aponta para o novo head (mantém circularidade)
            self.tail.next = novo_nodo

            # Atualiza o head para o novo nodo
            self.head = novo_nodo

    def append(self, dado):
        """Insere um novo nodo no final da lista"""
        # Cria um novo nodo com o dado
        novo_nodo = Node(dado)

        # Caso especial: lista vazia
        if self.head is None:
            self.head = novo_nodo
            self.tail = novo_nodo
            novo_nodo.next = novo_nodo  # Circular: aponta para si mesmo
            novo_nodo.prev = novo_nodo  # Circular: aponta para si mesmo
        else:
            # Conecta o novo nodo na estrutura circular
            # O próximo do novo nodo aponta para o head (circularidade)
            novo_nodo.next = self.head

            # O anterior do novo nodo aponta para o antigo tail
            novo_nodo.prev = self.tail

            # O próximo do antigo tail aponta para o novo nodo
            self.tail.next = novo_nodo

            # O anterior do head aponta para o novo tail (mantém circularidade)
            self.head.prev = novo_nodo

            # Atualiza o tail para o novo nodo
            self.tail = novo_nodo

    def insert_at(self, dado, index):
        """Insere um novo nodo em uma posição específica da lista"""
        # Caso especial: inserção no início
        if index == 0:
            self.prepend(dado)
            return True

        # Caso especial: lista vazia e índice > 0
        if self.head is None:
            print("Erro: A lista está vazia. Use índice 0 para inserir.")
            return False

        # Cria o novo nodo
        novo_nodo = Node(dado)

        # Variáveis para percorrer a lista
        nodo_atual = self.head
        posicao = 0

        # Percorre até a posição desejada
        while posicao < index:
            nodo_atual = nodo_atual.next

            # Se voltou ao head, verificamos se é inserção no final
            if nodo_atual == self.head:
                # Se a posição é exatamente após o último elemento
                if posicao == index - 1:
                    self.append(dado)
                    return True
                else:
                    print(f"Erro: A lista tem apenas {posicao + 1} elementos")
                    return False

            posicao += 1

        # Obtém o nodo anterior através do ponteiro prev
        # Vantagem da lista dupla: acesso direto ao anterior!
        nodo_anterior = nodo_atual.prev

        # Conecta o novo nodo na posição correta
        novo_nodo.next = nodo_atual
        novo_nodo.prev = nodo_anterior

        # Atualiza as referências dos nodos adjacentes
        nodo_anterior.next = novo_nodo
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
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # O novo head será o segundo nodo
            novo_head = self.head.next

            # O anterior do novo head aponta para o tail (circularidade)
            novo_head.prev = self.tail

            # O próximo do tail aponta para o novo head (circularidade)
            self.tail.next = novo_head

            # Atualiza o head
            self.head = novo_head

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
            # O novo tail será o penúltimo nodo
            # Vantagem da lista dupla circular: acesso direto via tail.prev!
            novo_tail = self.tail.prev

            # O próximo do novo tail aponta para o head (circularidade)
            novo_tail.next = self.head

            # O anterior do head aponta para o novo tail (circularidade)
            self.head.prev = novo_tail

            # Atualiza o tail
            self.tail = novo_tail

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
        while posicao < index:
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

        # Obtém os nodos adjacentes através dos ponteiros
        nodo_anterior = nodo_atual.prev
        nodo_proximo = nodo_atual.next

        # Reconecta os nodos adjacentes, "pulando" o nodo removido
        nodo_anterior.next = nodo_proximo
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
        nodo_atual = self.head.next  # Começa do segundo nodo

        # Continua enquanto não voltar ao head
        while nodo_atual != self.head:
            if nodo_atual.dado == dado:
                # Obtém os nodos adjacentes
                nodo_anterior = nodo_atual.prev
                nodo_proximo = nodo_atual.next

                # Reconecta os nodos
                nodo_anterior.next = nodo_proximo
                nodo_proximo.prev = nodo_anterior

                return True

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
        """Retorna o dado em uma posição específica (busca otimizada)"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Erro: A lista está vazia")
            return None

        # Caso especial: índice negativo
        if index < 0:
            print("Erro: O índice deve ser um número positivo")
            return None

        # Obtém o tamanho para validação e otimização
        tamanho = self.size()

        # Verifica se o índice está nos limites
        if index >= tamanho:
            print(f"Erro: Índice {index} fora dos limites da lista")
            return None

        # Otimização: decide se busca pelo início ou pelo fim
        # Vantagem da lista dupla circular: podemos ir em qualquer direção!
        if index <= tamanho // 2:
            # Busca a partir do head (início) - mais perto do começo
            nodo_atual = self.head
            for _ in range(index):
                nodo_atual = nodo_atual.next
        else:
            # Busca a partir do tail (fim) - mais perto do final
            nodo_atual = self.tail
            passos_do_fim = tamanho - 1 - index
            for _ in range(passos_do_fim):
                nodo_atual = nodo_atual.prev

        return nodo_atual.dado

    # ==================== MÉTODOS DE TRAVESSIA ====================

    def traversal(self):
        """Percorre e exibe todos os elementos da lista (head -> tail)"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return

        # Inicia a varredura a partir do head
        nodo_atual = self.head
        elementos = []
        index = 0

        # Percorre toda a lista (do-while: executa pelo menos uma vez)
        while True:
            elementos.append(f"[{index}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.next
            index += 1

            # Para quando voltar ao head (completou o ciclo)
            if nodo_atual == self.head:
                break

        # Exibe com setas bidirecionais e indicação de circularidade
        print(" <-> ".join(elementos) + " <-> (volta ao início)")

    def traversal_reverso(self):
        """Percorre e exibe todos os elementos da lista (tail -> head)"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return

        # Inicia a varredura a partir do tail
        nodo_atual = self.tail
        elementos = []
        index = self.size() - 1

        # Percorre toda a lista usando o ponteiro prev
        while True:
            elementos.append(f"[{index}] {nodo_atual.dado}")
            nodo_atual = nodo_atual.prev
            index -= 1

            # Para quando voltar ao tail (completou o ciclo reverso)
            if nodo_atual == self.tail:
                break

        # Exibe com setas bidirecionais e indicação de circularidade
        print(" <-> ".join(elementos) + " <-> (volta ao final)")

    def demonstrar_circularidade_frente(self, voltas=2):
        """Demonstra a circularidade percorrendo a lista para frente N vezes"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return

        print(f"\n{'='*60}")
        print(f"  DEMONSTRAÇÃO DE CIRCULARIDADE - SENTIDO HORÁRIO (FRENTE)")
        print(f"  Iniciando do HEAD, seguindo pelos ponteiros NEXT")
        print(f"{'='*60}")

        # Calcula quantos elementos exibir
        tamanho = self.size()
        total_elementos = tamanho * voltas

        # Inicia do head, seguindo para frente (next)
        nodo_atual = self.head
        volta_atual = 1

        print(f"\n>>> Volta {volta_atual}:")
        elementos_volta = []

        for i in range(total_elementos):
            # Detecta início de nova volta
            if i > 0 and i % tamanho == 0:
                # Exibe a volta anterior
                print("    " + " -> ".join(elementos_volta))
                volta_atual += 1
                print(f"\n>>> Volta {volta_atual} (retornou ao HEAD):")
                elementos_volta = []

            elementos_volta.append(nodo_atual.dado)
            nodo_atual = nodo_atual.next

        # Exibe a última volta
        print("    " + " -> ".join(elementos_volta))

        print(f"\n[✓] Completou {voltas} volta(s) usando head.next sucessivamente")
        print(f"[✓] Prova que tail.next = head (circularidade)")

    def demonstrar_circularidade_tras(self, voltas=2):
        """Demonstra a circularidade percorrendo a lista para trás N vezes"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return

        print(f"\n{'='*60}")
        print(f"  DEMONSTRAÇÃO DE CIRCULARIDADE - SENTIDO ANTI-HORÁRIO (TRÁS)")
        print(f"  Iniciando do TAIL, seguindo pelos ponteiros PREV")
        print(f"{'='*60}")

        # Calcula quantos elementos exibir
        tamanho = self.size()
        total_elementos = tamanho * voltas

        # Inicia do tail, seguindo para trás (prev)
        nodo_atual = self.tail
        volta_atual = 1

        print(f"\n>>> Volta {volta_atual}:")
        elementos_volta = []

        for i in range(total_elementos):
            # Detecta início de nova volta
            if i > 0 and i % tamanho == 0:
                # Exibe a volta anterior
                print("    " + " <- ".join(elementos_volta))
                volta_atual += 1
                print(f"\n>>> Volta {volta_atual} (retornou ao TAIL):")
                elementos_volta = []

            elementos_volta.append(nodo_atual.dado)
            nodo_atual = nodo_atual.prev

        # Exibe a última volta
        print("    " + " <- ".join(elementos_volta))

        print(f"\n[✓] Completou {voltas} volta(s) usando tail.prev sucessivamente")
        print(f"[✓] Prova que head.prev = tail (circularidade reversa)")

    def demonstrar_circularidade_completa(self, voltas=2):
        """Demonstra a circularidade em ambas as direções"""
        # Caso especial: lista vazia
        if self.head is None:
            print("Lista vazia")
            return

        tamanho = self.size()

        print(f"\n{'='*60}")
        print(f"  DEMONSTRAÇÃO COMPLETA DE CIRCULARIDADE BIDIRECIONAL")
        print(f"{'='*60}")

        # Informações da estrutura
        print(f"\n[ESTRUTURA DA LISTA]")
        print(f"  Tamanho: {tamanho} elementos")
        print(f"  Head (primeiro): '{self.head.dado}'")
        print(f"  Tail (último):   '{self.tail.dado}'")
        print(f"\n[CONEXÕES CIRCULARES]")
        print(f"  head.prev = '{self.head.prev.dado}' (deve ser tail)")
        print(f"  tail.next = '{self.tail.next.dado}' (deve ser head)")

        # Demonstração para frente
        print(f"\n{'-'*60}")
        print(f"PARTE 1: Percorrendo para FRENTE (usando .next)")
        print(f"{'-'*60}")

        nodo_atual = self.head
        for v in range(voltas):
            elementos = []
            for _ in range(tamanho):
                elementos.append(nodo_atual.dado)
                nodo_atual = nodo_atual.next
            print(f"  Volta {v+1}: {' -> '.join(elementos)} -> [volta ao head]")

        # Demonstração para trás
        print(f"\n{'-'*60}")
        print(f"PARTE 2: Percorrendo para TRÁS (usando .prev)")
        print(f"{'-'*60}")

        nodo_atual = self.tail
        for v in range(voltas):
            elementos = []
            for _ in range(tamanho):
                elementos.append(nodo_atual.dado)
                nodo_atual = nodo_atual.prev
            print(f"  Volta {v+1}: {' <- '.join(elementos)} <- [volta ao tail]")

        # Demonstração alternada (zig-zag)
        print(f"\n{'-'*60}")
        print(f"PARTE 3: Navegação ZIG-ZAG (alternando direções)")
        print(f"{'-'*60}")

        nodo_atual = self.head
        passos = []
        passos.append(f"Início: {nodo_atual.dado}")

        # Vai para frente 2 passos
        for _ in range(2):
            nodo_atual = nodo_atual.next
            passos.append(f"-> {nodo_atual.dado}")

        # Volta 1 passo
        nodo_atual = nodo_atual.prev
        passos.append(f"<- {nodo_atual.dado}")

        # Vai para frente até dar a volta
        for _ in range(tamanho):
            nodo_atual = nodo_atual.next
            passos.append(f"-> {nodo_atual.dado}")

        print(f"  {' '.join(passos[:8])}")
        if len(passos) > 8:
            print(f"  {' '.join(passos[8:])}")

        print(f"\n{'='*60}")
        print(f"[✓] Lista circular duplamente encadeada verificada!")
        print(f"[✓] Navegação bidirecional funcionando corretamente!")
        print(f"{'='*60}")

    # ==================== MÉTODOS AUXILIARES ====================

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

    def get_head(self):
        """Retorna o dado do primeiro elemento (head)"""
        if self.head is None:
            return None
        return self.head.dado

    def get_tail(self):
        """Retorna o dado do último elemento (tail)"""
        if self.tail is None:
            return None
        return self.tail.dado


# ==================== FUNÇÕES DO MENU ====================

def exibir_menu():
    """Exibe o menu de opções para o usuário"""
    print("\n" + "=" * 60)
    print("      GERENCIADOR DE LISTA CIRCULAR DUPLAMENTE ENCADEADA")
    print("=" * 60)
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
    print("13. Exibir head e tail")
    print("\n--- DEMONSTRAÇÃO DE CIRCULARIDADE ---")
    print("14. Demonstrar circularidade (FRENTE)")
    print("15. Demonstrar circularidade (TRÁS)")
    print("16. Demonstrar circularidade COMPLETA (ambas direções)")
    print("\n--- SISTEMA ---")
    print("17. Carregar dados de exemplo")
    print("0. Sair")
    print("=" * 60)


def carregar_exemplo(lista):
    """Carrega dados de exemplo na lista para demonstração"""
    # Limpa a lista atual
    lista.head = None
    lista.tail = None

    # Insere os personagens das Tartarugas Ninja
    # Imagine uma mesa redonda de reunião onde todos se veem!
    lista.append('Leonardo')      # O líder, usa espadas katana
    lista.append('Raphael')       # O valentão, usa sais
    lista.append('Donatello')     # O gênio, usa bastão bo
    lista.append('Michelangelo')  # O engraçado, usa nunchakus

    print("Dados de exemplo carregados com sucesso!")
    print("Tartarugas Ninja em formação circular de reunião!")
    print("(Cada um pode ver quem está à sua frente E atrás)")


def main():
    """Função principal com menu interativo"""
    # Cria uma nova lista circular duplamente encadeada vazia
    lista = CircularDoublyLinkedList()

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
            print("\nObrigado por usar o Gerenciador de Lista Circular Dupla!")
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

        # ===== Opção 13: Exibir head e tail =====
        elif opcao == '13':
            if lista.is_empty():
                print("A lista está vazia.")
            else:
                print(f"\n--- Informações de Head e Tail ---")
                print(f"Head (primeiro): '{lista.get_head()}'")
                print(f"Tail (último):   '{lista.get_tail()}'")
                print(f"\n--- Conexões Circulares ---")
                print(f"Head.prev: '{lista.head.prev.dado}' (deve ser o tail)")
                print(f"Tail.next: '{lista.tail.next.dado}' (deve ser o head)")

        # ===== Opção 14: Demonstrar circularidade (FRENTE) =====
        elif opcao == '14':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            try:
                voltas = int(input("Quantas voltas deseja visualizar? (1-5): "))
                if voltas < 1 or voltas > 5:
                    print("Erro: Digite um número entre 1 e 5.")
                    continue
                lista.demonstrar_circularidade_frente(voltas)
            except ValueError:
                print("Erro: Digite um número inteiro válido.")

        # ===== Opção 15: Demonstrar circularidade (TRÁS) =====
        elif opcao == '15':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            try:
                voltas = int(input("Quantas voltas deseja visualizar? (1-5): "))
                if voltas < 1 or voltas > 5:
                    print("Erro: Digite um número entre 1 e 5.")
                    continue
                lista.demonstrar_circularidade_tras(voltas)
            except ValueError:
                print("Erro: Digite um número inteiro válido.")

        # ===== Opção 16: Demonstrar circularidade COMPLETA =====
        elif opcao == '16':
            if lista.is_empty():
                print("Erro: A lista está vazia.")
                continue
            try:
                voltas = int(input("Quantas voltas em cada direção? (1-3): "))
                if voltas < 1 or voltas > 3:
                    print("Erro: Digite um número entre 1 e 3.")
                    continue
                lista.demonstrar_circularidade_completa(voltas)
            except ValueError:
                print("Erro: Digite um número inteiro válido.")

        # ===== Opção 17: Carregar dados de exemplo =====
        elif opcao == '17':
            carregar_exemplo(lista)
            lista.traversal()

        # ===== Opção inválida =====
        else:
            print("Opção inválida! Por favor, escolha uma opção de 0 a 17.")


# Ponto de entrada do programa
# Só executa a main() se o arquivo for executado diretamente
if __name__ == "__main__":
    main()