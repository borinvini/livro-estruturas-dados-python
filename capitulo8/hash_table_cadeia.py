class Node:
    """
    Nó da lista encadeada para tratamento de colisões.
    """
    
    def __init__(self, chave=None):
        self.chave = chave
        self.next = None


class ListaEncadeada:
    """
    Lista encadeada que armazena as chaves em cada posição da tabela.
    """
    
    def __init__(self):
        self.head = None
    
    def inserir_no_inicio(self, chave):
        """
        Insere uma chave no início da lista encadeada.
        
        Inserir no início é O(1), tornando a operação eficiente
        independente do tamanho da cadeia.
        """
        novo_nodo = Node(chave)
        novo_nodo.next = self.head
        self.head = novo_nodo
    
    def buscar(self, chave):
        """
        Busca uma chave na lista encadeada.
        
        Percorre a lista do início ao fim procurando a chave.
        No pior caso, examina todos os elementos (O(n) onde n é
        o tamanho da cadeia).
        
        Retorna:
            Node: O nó contendo a chave, ou None se não encontrada
        """
        atual = self.head
        while atual is not None:
            if atual.chave == chave:
                return atual
            atual = atual.next
        return None
    
    def remover(self, chave):
        """
        Remove uma chave da lista encadeada.
        
        Trata dois casos especiais:
        1. Remoção do primeiro elemento (head)
        2. Remoção de elemento no meio ou fim da lista
        
        Retorna:
            bool: True se removeu, False se não encontrou
        """
        atual = self.head
        anterior = None
        
        while atual is not None:
            if atual.chave == chave:
                if anterior is None:
                    # Removendo o primeiro elemento
                    self.head = atual.next
                else:
                    # Removendo elemento do meio ou fim
                    anterior.next = atual.next
                return True
            anterior = atual
            atual = atual.next
        
        return False
    
    def esta_vazia(self):
        """Verifica se a lista está vazia."""
        return self.head is None
    
    def contar(self):
        """Conta quantos elementos estão na lista."""
        contador = 0
        atual = self.head
        while atual is not None:
            contador += 1
            atual = atual.next
        return contador
    
    def listar_chaves(self):
        """Retorna uma lista com todas as chaves."""
        resultado = []
        atual = self.head
        while atual is not None:
            resultado.append(atual.chave)
            atual = atual.next
        return resultado


class TabelaHashEncadeada:
    """
    Tabela Hash com tratamento de colisões por encadeamento.
    
    Diferente da tabela hash simples (endereçamento aberto), cada posição
    da tabela contém uma lista encadeada. Quando ocorre uma colisão,
    o novo elemento é simplesmente adicionado à lista daquela posição.
    
    Vantagens do encadeamento:
        - Nunca "enche" completamente (pode ter mais elementos que posições)
        - Remoção é simples (não precisa de marcadores especiais)
        - Desempenho degrada gradualmente com colisões
    
    Desvantagens:
        - Usa memória extra para os ponteiros dos nós
        - Perde localidade de cache (nós espalhados na memória)
    
    Atributos:
        tamanho (int): Número de posições (buckets) na tabela
        tabela (list): Lista de listas encadeadas
        quantidade (int): Total de elementos armazenados
    """
    
    def __init__(self, tamanho=10):
        """
        Inicializa a tabela hash com encadeamento.
        
        Cada posição da tabela é inicializada com uma lista encadeada
        vazia, pronta para receber elementos.
        """
        self.tamanho = tamanho
        self.tabela = [ListaEncadeada() for _ in range(tamanho)]
        self.quantidade = 0
        
        print(f"Tabela Hash Encadeada criada com {tamanho} posições.")
    
    def _hash_function(self, chave):
        """
        Calcula a posição na tabela usando a função hash.
        
        Para siglas (strings de 2 caracteres):
            - Soma os códigos ASCII das duas letras
            - Aplica módulo pelo tamanho da tabela
        """
        chave = chave.upper()
        codigo_primeira = ord(chave[0])
        codigo_segunda = ord(chave[1])
        soma = codigo_primeira + codigo_segunda
        posicao = soma % self.tamanho
        
        # Exibe o cálculo para fins didáticos
        print(f"\n--- Cálculo do Hash para '{chave}' ---")
        print(f"    ord('{chave[0]}') = {codigo_primeira}")
        print(f"    ord('{chave[1]}') = {codigo_segunda}")
        print(f"    Soma = {codigo_primeira} + {codigo_segunda} = {soma}")
        print(f"    Posição = {soma} % {self.tamanho} = {posicao}")
        
        return posicao
    
    def inserir(self, chave):
        """
        Insere uma chave na tabela hash.
        
        Com encadeamento, colisões são tratadas naturalmente:
        a nova chave é adicionada à lista encadeada da posição.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return False
        
        posicao = self._hash_function(chave)
        
        # Verifica se já existe (evita duplicatas)
        if self.tabela[posicao].buscar(chave) is not None:
            print(f"\n'{chave}' já existe na posição {posicao}!")
            return False
        
        # Verifica se haverá colisão (para fins didáticos)
        if not self.tabela[posicao].esta_vazia():
            existentes = self.tabela[posicao].listar_chaves()
            print(f"\nCOLISÃO detectada na posição {posicao}!")
            print(f"    Elementos já presentes: {existentes}")
            print(f"    Adicionando '{chave}' à cadeia...")
        
        # Insere na lista encadeada da posição
        self.tabela[posicao].inserir_no_inicio(chave)
        self.quantidade += 1
        
        tamanho_cadeia = self.tabela[posicao].contar()
        print(f"\n'{chave}' inserida na posição {posicao}!")
        print(f"    Tamanho da cadeia: {tamanho_cadeia} elemento(s)")
        
        return True
    
    def remover(self, chave):
        """
        Remove uma chave da tabela hash.
        
        Com encadeamento, a remoção é simples: basta remover
        o nó da lista encadeada correspondente.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return False
        
        posicao = self._hash_function(chave)
        
        if self.tabela[posicao].remover(chave):
            self.quantidade -= 1
            print(f"\n'{chave}' removida com sucesso da posição {posicao}!")
            return True
        else:
            print(f"\n'{chave}' não encontrada na posição {posicao}.")
            return False
    
    def buscar(self, chave):
        """
        Busca uma chave na tabela hash.
        
        Calcula a posição e percorre a lista encadeada
        procurando a chave desejada.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return -1
        
        posicao = self._hash_function(chave)
        
        if self.tabela[posicao].buscar(chave) is not None:
            print(f"\n'{chave}' encontrada na posição {posicao}!")
            cadeia = self.tabela[posicao].listar_chaves()
            print(f"    Cadeia completa: {cadeia}")
            return posicao
        else:
            print(f"\n'{chave}' não encontrada na tabela.")
            return -1
    
    def exibir(self):
        """Exibe a tabela hash de forma visual e organizada."""
        print("\n" + "=" * 55)
        print("       ESTADO ATUAL DA TABELA HASH (ENCADEAMENTO)")
        print("=" * 55)
        print(f"  {'Índice':<8} {'Cadeia':<35} {'Tam.':<6}")
        print("-" * 55)
        
        for indice, lista in enumerate(self.tabela):
            chaves = lista.listar_chaves()
            tamanho = len(chaves)
            
            if tamanho == 0:
                print(f"    {indice:<8} {'[vazio]':<35} {0:<6}")
            else:
                # Formata a cadeia como: SP → RJ → None
                cadeia_str = " → ".join(chaves) + " → None"
                if len(cadeia_str) > 33:
                    cadeia_str = cadeia_str[:30] + "..."
                print(f"    {indice:<8} {cadeia_str:<35} {tamanho:<6}")
        
        print("-" * 55)
        print(f"  Total de elementos: {self.quantidade}")
        print(f"  Fator de carga: {self.fator_carga():.1%}")
        print(f"  Maior cadeia: {self._maior_cadeia()} elemento(s)")
        print("=" * 55)
    
    def fator_carga(self):
        """
        Calcula o fator de carga da tabela hash.
        
        Com encadeamento, o fator de carga pode ser maior que 1.0
        (mais elementos que posições), mas valores muito altos
        indicam cadeias longas e busca lenta.
        
        Retorna:
            float: Razão entre elementos armazenados e tamanho da tabela
        """
        return self.quantidade / self.tamanho
    
    def _maior_cadeia(self):
        """Retorna o tamanho da maior cadeia (métrica de distribuição)."""
        return max(lista.contar() for lista in self.tabela)
    
    def __len__(self):
        """Retorna a quantidade de elementos na tabela (permite usar len())."""
        return self.quantidade
    
    def __str__(self):
        """Representação em string da tabela (permite usar print())."""
        elementos = []
        for i, lista in enumerate(self.tabela):
            chaves = lista.listar_chaves()
            if chaves:
                elementos.append(f"{i}:{chaves}")
        return f"TabelaHashEncadeada({', '.join(elementos) if elementos else 'vazia'})"
    
    def __contains__(self, chave):
        """Permite usar o operador 'in' para verificar existência."""
        chave = chave.upper()
        if len(chave) != 2:
            return False
        posicao = (ord(chave[0]) + ord(chave[1])) % self.tamanho
        return self.tabela[posicao].buscar(chave) is not None


# =============================================================================
# FUNÇÕES AUXILIARES DO PROGRAMA
# =============================================================================

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n" + "-" * 40)
    print("   MENU - TABELA HASH (ENCADEAMENTO)")
    print("-" * 40)
    print("  1 - Inserir sigla")
    print("  2 - Remover sigla")
    print("  3 - Buscar sigla")
    print("  4 - Exibir tabela")
    print("  5 - Inserir exemplos (teste)")
    print("  6 - Sair")
    print("-" * 40)


def main():
    
    # Cria uma instância da tabela hash encadeada
    tabela = TabelaHashEncadeada(tamanho=10)
    
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nDigite um número válido!")
            continue
        
        if opcao == 1:
            sigla = input("Digite a sigla do estado (2 letras): ")
            tabela.inserir(sigla)
        
        elif opcao == 2:
            sigla = input("Digite a sigla a remover: ")
            tabela.remover(sigla)
        
        elif opcao == 3:
            sigla = input("Digite a sigla a buscar: ")
            tabela.buscar(sigla)
        
        elif opcao == 4:
            tabela.exibir()
        
        elif opcao == 5:
            # Insere várias siglas para demonstrar colisões
            print("\n>>> Inserindo siglas de teste...")
            siglas_teste = ["SP", "RJ", "MG", "BA", "RS", "PR", "SC", "PE", "CE", "GO",
                           "PA", "MA", "PB", "AM", "RN"]
            for sigla in siglas_teste:
                tabela.inserir(sigla)
            print("\n>>> Teste concluído!")
        
        elif opcao == 6:
            print("\n" + "=" * 50)
            print(f"  Tabela final: {tabela}")
            print("  Programa encerrado. Até a próxima!")
            print("=" * 50)
            break
        
        else:
            print("\nOpção inválida!")


# =============================================================================
# PONTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    main()