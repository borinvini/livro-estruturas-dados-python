class TabelaHash:
    """
    Classe que implementa uma Tabela Hash com tratamento de colisões
    por Tentativa Linear (Linear Probing).
    
    Atributos:
        tamanho (int): Número de posições disponíveis na tabela
        tabela (list): Lista que armazena os elementos
        quantidade (int): Número de elementos atualmente armazenados
    """
    
    def __init__(self, tamanho=10):
        """
        Inicializa a tabela hash.
        """
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.quantidade = 0
        
        print(f"Tabela Hash criada com {tamanho} posições.")
    
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
    
    def _tentativa_linear(self, chave, posicao_inicial):
        """
        Percorre a tabela linearmente a partir da posição inicial.
        
        Retorna a posição onde:
        - A chave foi encontrada, OU
        - Há uma posição vazia (None)
        
        Retorna -1 se a tabela foi completamente percorrida sem 
        encontrar a chave nem posição vazia.
        """
        tentativa = posicao_inicial
        colisoes = 0
        
        print(f">>> Iniciando Tentativa Linear na posição {posicao_inicial}")
        
        while True:
            valor_atual = self.tabela[tentativa]
            
            # Encontrou posição vazia ou a própria chave
            if valor_atual is None or valor_atual == chave:
                if colisoes > 0:
                    print(f"Posição {tentativa} disponível "
                        f"após {colisoes} colisão(ões)")
                return tentativa
            
            # Posição ocupada por outra chave - continua buscando
            colisoes += 1
            print(f"Colisão #{colisoes}: "
                f"posição {tentativa} ocupada por '{valor_atual}'")
            
            # Avança para próxima posição (circular)
            tentativa = (tentativa + 1) % self.tamanho
            
            # Se voltou ao início, tabela foi completamente percorrida
            if tentativa == posicao_inicial:
                print(f">>> Tabela completamente percorrida! "
                    f"Não há posições disponíveis.")
                return -1
    
    def inserir(self, chave):
        """
        Insere uma chave na tabela hash.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return False
        
        posicao_inicial = self._hash_function(chave)
        posicao_final = self._tentativa_linear(chave, posicao_inicial)
        
        # Tabela cheia
        if posicao_final == -1:
            print(f"\nErro: Tabela cheia! Não foi possível inserir '{chave}'.")
            return False
        
        # Chave já existe
        if self.tabela[posicao_final] == chave:
            print(f"\nErro: '{chave}' já existe na posição {posicao_final}!")
            return False
        
        # Inserção bem-sucedida
        self.tabela[posicao_final] = chave
        self.quantidade += 1
        
        if posicao_final == posicao_inicial:
            print(f"\n'{chave}' inserida na posição {posicao_final} (posição ideal)!")
        else:
            print(f"\n'{chave}' inserida na posição {posicao_final} (deslocada de {posicao_inicial})!")
        
        return True
    
    def buscar(self, chave):
        """
        Busca uma chave na tabela hash.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return -1
        
        posicao_inicial = self._hash_function(chave)
        posicao_encontrada = self._tentativa_linear(chave, posicao_inicial)
        
        # Verificar se encontrou a chave ou posição vazia
        if posicao_encontrada != -1 and self.tabela[posicao_encontrada] == chave:
            print(f"\n'{chave}' encontrada na posição {posicao_encontrada}!")
            return posicao_encontrada
        else:
            print(f"\n'{chave}' não encontrada na tabela.")
            return -1
    
    def remover(self, chave):
        """
        Remove uma chave da tabela hash.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return False
        
        posicao_inicial = self._hash_function(chave)
        posicao_encontrada = self._tentativa_linear(chave, posicao_inicial)
        
        if posicao_encontrada != -1 and self.tabela[posicao_encontrada] == chave:
            self.tabela[posicao_encontrada] = None
            self.quantidade -= 1
            print(f"\n'{chave}' removida com sucesso da posição {posicao_encontrada}!")
            return True
        else:
            print(f"\n'{chave}' não encontrada na tabela.")
            return False
    
    def exibir(self):
        """Exibe a tabela hash de forma visual e organizada."""
        print("\n" + "=" * 45)
        print("          ESTADO ATUAL DA TABELA HASH")
        print("=" * 45)
        print(f"  {'Índice':<10} {'Conteúdo':<15} {'Status':<12}")
        print("-" * 45)
        
        for indice, valor in enumerate(self.tabela):
            if valor is None:
                print(f"    {indice:<10} {'---':<15} {'[vazio]':<12}")
            else:
                print(f"    {indice:<10} {valor:<15} {'[ocupado]':<12}")
        
        print("-" * 45)
        print(f"  Total de elementos: {self.quantidade}/{self.tamanho}")
        print(f"  Fator de carga: {self.fator_carga():.1%}")
        print("=" * 45)
    
    def fator_carga(self):
        """
        Calcula o fator de carga da tabela hash.
        
        O fator de carga indica o quão "cheia" está a tabela.
        Valores acima de 0.7 (70%) geralmente indicam necessidade de expansão.
        
        Retorna:
            float: Razão entre elementos armazenados e tamanho da tabela
        """
        return self.quantidade / self.tamanho
    
    def __len__(self):
        """Retorna a quantidade de elementos na tabela (permite usar len())."""
        return self.quantidade
    
    def __str__(self):
        """Representação em string da tabela (permite usar print())."""
        elementos = [f"{i}:{v}" for i, v in enumerate(self.tabela) if v is not None]
        return f"TabelaHash({', '.join(elementos) if elementos else 'vazia'})"
    
    def __contains__(self, chave):
        """Permite usar o operador 'in' para verificar existência."""
        chave = chave.upper()
        if len(chave) != 2:
            return False
        posicao = (ord(chave[0]) + ord(chave[1])) % self.tamanho
        return self.tabela[posicao] == chave


# =============================================================================
# FUNÇÕES AUXILIARES DO PROGRAMA
# =============================================================================

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n" + "-" * 35)
    print("   MENU - TABELA HASH")
    print("-" * 35)
    print("  1 - Inserir sigla")
    print("  2 - Remover sigla")
    print("  3 - Buscar sigla")
    print("  4 - Exibir tabela")
    print("  5 - Sair")
    print("-" * 35)


def main():
    
    # Cria uma instância da tabela hash
    tabela = TabelaHash(tamanho=10)
    
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n⚠ Digite um número válido!")
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
            print("\n" + "=" * 50)
            print(f"  Tabela final: {tabela}")
            print("  Programa encerrado. Até a próxima!")
            print("=" * 50)
            break
        
        else:
            print("\n⚠ Opção inválida!")


# =============================================================================
# DEMONSTRAÇÃO DE COLISÕES
# =============================================================================

def demonstracao_colisoes():
    """
    Demonstra o funcionamento do tratamento de colisões por tentativa linear.
    
    Utiliza siglas de estados brasileiros que propositalmente geram
    o mesmo valor hash, forçando colisões para fins didáticos.
    """
    print("\n" + "=" * 65)
    print("       DEMONSTRAÇÃO: TRATAMENTO DE COLISÕES POR TENTATIVA LINEAR")
    print("=" * 65)
    
    print("\n" + "-" * 65)
    print("  PARTE 1: Entendendo as colisões")
    print("-" * 65)
    print("""
  Três siglas de estados brasileiros podem ter o MESMO hash se 
  a soma dos códigos ASCII resultar no mesmo resto. Por exemplo:
  
    SP: ord('S') + ord('P') = 83 + 80 = 163  →  163 % 10 = 3
    PI: ord('P') + ord('I') = 80 + 73 = 153  →  153 % 10 = 3
    TO: ord('T') + ord('O') = 84 + 79 = 163  →  163 % 10 = 3
  
  Todas as três querem ocupar a posição 3! Isso é uma COLISÃO.
  A tentativa linear resolve buscando a próxima posição livre.
    """)
    
    input("  Pressione ENTER para ver a demonstração...")
    
    # Cria tabela pequena para facilitar visualização
    tabela = TabelaHash(tamanho=10)
    
    print("\n" + "-" * 65)
    print("  PARTE 2: Inserindo elementos com colisão")
    print("-" * 65)
    
    # Siglas que colidem (mesmo hash = 3)
    siglas_colisao = ['SP', 'PI', 'TO']
    
    for sigla in siglas_colisao:
        print(f"\n>>> Inserindo '{sigla}'...")
        tabela.inserir(sigla)
        input("    Pressione ENTER para continuar...")
    
    tabela.exibir()
    
    print("\n" + "-" * 65)
    print("  PARTE 3: Buscando elementos deslocados")
    print("-" * 65)
    print("""
  Quando buscamos um elemento que foi deslocado por colisão,
  a tentativa linear percorre as posições até encontrá-lo.
    """)
    
    input("  Pressione ENTER para buscar 'TO' (deslocada para posição 5)...")
    tabela.buscar('TO')
    
    print("\n" + "-" * 65)
    print("  PARTE 4: Inserindo mais elementos")
    print("-" * 65)
    
    # Outras siglas sem colisão
    outras_siglas = ['RJ', 'MG', 'BA']
    
    for sigla in outras_siglas:
        print(f"\n>>> Inserindo '{sigla}'...")
        tabela.inserir(sigla)
    
    tabela.exibir()
    
    print("\n" + "-" * 65)
    print("  PARTE 5: Tentando inserir elemento duplicado")
    print("-" * 65)
    
    input("  Pressione ENTER para tentar inserir 'SP' novamente...")
    tabela.inserir('SP')
    
    print("\n" + "-" * 65)
    print("  PARTE 6: Buscando elemento inexistente")
    print("-" * 65)
    
    input("  Pressione ENTER para buscar 'XX' (não existe)...")
    tabela.buscar('XX')
    
    print("\n" + "=" * 65)
    print("  FIM DA DEMONSTRAÇÃO")
    print("=" * 65)
    print(f"\n  Estado final: {tabela}")
    print()
    
    return tabela


# =============================================================================
# PONTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("        TABELA HASH - TENTATIVA LINEAR")
    print("=" * 50)
    print("\n  Escolha o modo de execução:")
    print("    1 - Menu interativo")
    print("    2 - Demonstração de colisões")
    print()
    
    try:
        modo = int(input("  Opção: "))
    except ValueError:
        modo = 1
    
    if modo == 2:
        demonstracao_colisoes()
    else:
        main()