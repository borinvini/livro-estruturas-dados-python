class TabelaHash:
    """
    Classe que implementa uma Tabela Hash com tratamento de colisões
    por Tentativa Quadrática (Quadratic Probing).
    
    Atributos:
        tamanho (int): Número de posições disponíveis na tabela
        tabela (list): Lista que armazena os elementos
        quantidade (int): Número de elementos atualmente armazenados
    """
    
    def __init__(self, tamanho=10):
        """
        Inicializa a tabela hash.
        
        Observação: Para garantir que a tentativa quadrática visite
        todas as posições, é recomendado que o tamanho seja um número primo.
        """
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.quantidade = 0
        
        print(f"Tabela Hash criada com {tamanho} posições.")
        print("Método de tratamento de colisões: TENTATIVA QUADRÁTICA")
    
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
    
    def _tentativa_quadratica(self, chave, pos_ini):
            """
            Percorre a tabela usando incrementos quadráticos a partir da 
            posição inicial.
            
            Retorna a posição onde:
            - A chave foi encontrada, OU
            - Há uma posição vazia (None)
            
            Retorna -1 se todas as tentativas falharam (tabela pode estar cheia
            ou a sequência quadrática não cobre todas as posições).
            """
            print(f"    >>> Tentativa Quadrática a partir da posição {pos_ini}")
            print(f"        Fórmula: posição = ({pos_ini} + i²) % {self.tamanho}")
            
            for i in range(self.tamanho):
                # Calcula a posição usando incremento quadrático
                incremento = i * i  # i² = 0, 1, 4, 9, 16, 25, ...
                tentativa = (pos_ini + incremento) % self.tamanho
                valor_atual = self.tabela[tentativa]
                
                # Mostra o cálculo para fins didáticos
                if i > 0:
                    print(f"        Tentativa {i}: "
                        f"({pos_ini} + {i}²) % {self.tamanho} = "
                        f"({pos_ini} + {incremento}) % {self.tamanho} "
                        f"= {tentativa}", end="")
                
                # Encontrou posição vazia ou a própria chave
                if valor_atual is None or valor_atual == chave:
                    if i > 0:
                        if valor_atual is None:
                            print(f" → [vazio]")
                        else:
                            print(f" → encontrado!")
                        print(f"    >>> Posição {tentativa} disponível "
                            f"após {i} tentativa(s)")
                    return tentativa
                
                # Posição ocupada por outra chave - mostra e continua
                if i > 0:
                    print(f" → ocupado por '{valor_atual}'")
            
            # Todas as tentativas falharam
            print(f"    >>> Todas as {self.tamanho} tentativas falharam!")
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
        posicao_final = self._tentativa_quadratica(chave, posicao_inicial)
        
        # Tabela cheia ou sequência não encontrou posição livre
        if posicao_final == -1:
            print(f"\nErro: Não foi possível inserir '{chave}'.")
            print("       A tabela pode estar cheia ou a sequência quadrática")
            print("       não cobriu todas as posições.")
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
        posicao_encontrada = self._tentativa_quadratica(chave, posicao_inicial)
        
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
        
        ATENÇÃO: A remoção em tabelas com endereçamento aberto é problemática!
        Simplesmente colocar None pode "quebrar" a cadeia de busca.
        Uma solução comum é usar um marcador especial (DELETADO/TOMBSTONE).
        Para simplificar, esta implementação usa None diretamente.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return False
        
        posicao_inicial = self._hash_function(chave)
        posicao_encontrada = self._tentativa_quadratica(chave, posicao_inicial)
        
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
        print("\n" + "=" * 50)
        print("          ESTADO ATUAL DA TABELA HASH")
        print("          (Tentativa Quadrática)")
        print("=" * 50)
        print(f"  {'Índice':<10} {'Conteúdo':<15} {'Status':<12}")
        print("-" * 50)
        
        for indice, valor in enumerate(self.tabela):
            if valor is None:
                print(f"    {indice:<10} {'---':<15} {'[vazio]':<12}")
            else:
                print(f"    {indice:<10} {valor:<15} {'[ocupado]':<12}")
        
        print("-" * 50)
        print(f"  Total de elementos: {self.quantidade}/{self.tamanho}")
        print(f"  Fator de carga: {self.fator_carga():.1%}")
        print("=" * 50)
    
    def fator_carga(self):
        """
        Calcula o fator de carga da tabela hash.
        
        O fator de carga indica o quão "cheia" está a tabela.
        Valores acima de 0.5 (50%) já podem causar problemas
        na tentativa quadrática (recomendação mais conservadora
        que na tentativa linear).
        
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
        
        posicao_inicial = (ord(chave[0]) + ord(chave[1])) % self.tamanho
        
        for i in range(self.tamanho):
            tentativa = (posicao_inicial + i * i) % self.tamanho
            if self.tabela[tentativa] is None:
                return False
            if self.tabela[tentativa] == chave:
                return True
        return False


# =============================================================================
# FUNÇÕES AUXILIARES DO PROGRAMA
# =============================================================================

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n" + "-" * 40)
    print("   MENU - TABELA HASH (QUADRÁTICA)")
    print("-" * 40)
    print("  1 - Inserir sigla")
    print("  2 - Remover sigla")
    print("  3 - Buscar sigla")
    print("  4 - Exibir tabela")
    print("  5 - Sair")
    print("-" * 40)


def main():
    
    # Cria uma instância da tabela hash
    # Usando tamanho 11 (primo) para melhor distribuição na tentativa quadrática
    tabela = TabelaHash(tamanho=11)
    
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
# DEMONSTRAÇÃO DE COLISÕES COM TENTATIVA QUADRÁTICA
# =============================================================================

def demonstracao_colisoes():
    """
    Demonstra o funcionamento do tratamento de colisões por tentativa quadrática.
    
    Utiliza siglas de estados brasileiros que propositalmente geram
    o mesmo valor hash, forçando colisões para fins didáticos.
    """
    print("\n" + "=" * 70)
    print("      DEMONSTRAÇÃO: TRATAMENTO DE COLISÕES POR TENTATIVA QUADRÁTICA")
    print("=" * 70)
    
    print("\n" + "-" * 70)
    print("  PARTE 1: Entendendo a Tentativa Quadrática")
    print("-" * 70)
    print("""
  Na TENTATIVA LINEAR, quando há colisão, procuramos sequencialmente:
    posição = (hash + 1) % tamanho
    posição = (hash + 2) % tamanho
    posição = (hash + 3) % tamanho  ...e assim por diante.
  
  Na TENTATIVA QUADRÁTICA, usamos incrementos quadráticos (i²):
    posição = (hash + 1²) % tamanho = (hash + 1) % tamanho
    posição = (hash + 2²) % tamanho = (hash + 4) % tamanho
    posição = (hash + 3²) % tamanho = (hash + 9) % tamanho
  
  Sequência de incrementos: 0, 1, 4, 9, 16, 25, 36, 49, ...
  
  VANTAGEM: Reduz o "clustering primário" (agrupamento de elementos
  consecutivos) que ocorre na tentativa linear.
  
  OBSERVAÇÃO: É recomendado usar tamanho PRIMO para garantir que
  a sequência quadrática visite o máximo de posições possível.
    """)
    
    input("  Pressione ENTER para ver a demonstração...")
    
    # Cria tabela com tamanho primo para melhor funcionamento
    tabela = TabelaHash(tamanho=11)
    
    print("\n" + "-" * 70)
    print("  PARTE 2: Comparando os padrões de busca")
    print("-" * 70)
    print("""
  Exemplo com hash inicial = 3 e tamanho = 11:
  
  TENTATIVA LINEAR:        TENTATIVA QUADRÁTICA:
    3 + 0 = 3                3 + 0² = 3 + 0  = 3
    3 + 1 = 4                3 + 1² = 3 + 1  = 4
    3 + 2 = 5                3 + 2² = 3 + 4  = 7
    3 + 3 = 6                3 + 3² = 3 + 9  = 12 % 11 = 1
    3 + 4 = 7                3 + 4² = 3 + 16 = 19 % 11 = 8
    ...                      ...
  
  Note como a quadrática "pula" posições, evitando clustering!
    """)
    
    input("  Pressione ENTER para continuar...")
    
    print("\n" + "-" * 70)
    print("  PARTE 3: Inserindo elementos com colisão")
    print("-" * 70)
    
    # Siglas que colidem (mesmo hash = 9 para tamanho 11)
    # SP: (83 + 80) % 11 = 163 % 11 = 9
    # TO: (84 + 79) % 11 = 163 % 11 = 9
    # FC: (70 + 67) % 11 = 137 % 11 = 5 (não colide)
    
    siglas_colisao = ['SP', 'TO']  # Ambas têm hash = 9 (mod 11)
    
    print("\n  As siglas SP e TO colidem (mesmo hash):")
    print("    SP: (83 + 80) % 11 = 163 % 11 = 9")
    print("    TO: (84 + 79) % 11 = 163 % 11 = 9\n")
    
    for sigla in siglas_colisao:
        print(f"\n>>> Inserindo '{sigla}'...")
        tabela.inserir(sigla)
        input("    Pressione ENTER para continuar...")
    
    tabela.exibir()
    
    print("\n" + "-" * 70)
    print("  PARTE 4: Observando o padrão quadrático")
    print("-" * 70)
    print("""
  Observe que 'TO' foi inserido na posição 10, não na posição 10!
  
  Cálculo para 'TO' (hash = 9):
    Tentativa 0: (9 + 0²) % 11 = 9  → ocupado por 'SP'
    Tentativa 1: (9 + 1²) % 11 = 10 → vazio! Inserido aqui.
  
  Se fosse tentativa LINEAR, também iria para 10.
  A diferença aparece com mais colisões!
    """)
    
    input("  Pressione ENTER para adicionar mais elementos...")
    
    # Adicionando elemento que mostrará melhor o padrão quadrático
    # Vamos adicionar algo que force uma terceira colisão no índice 9
    print("\n  Inserindo 'PI' que também tem hash próximo...")
    
    outras_siglas = ['RJ', 'MG', 'BA', 'RS']
    
    for sigla in outras_siglas:
        print(f"\n>>> Inserindo '{sigla}'...")
        tabela.inserir(sigla)
    
    tabela.exibir()
    
    print("\n" + "-" * 70)
    print("  PARTE 5: Buscando elementos")
    print("-" * 70)
    
    input("  Pressione ENTER para buscar 'TO' (deslocada por colisão)...")
    tabela.buscar('TO')
    
    print("\n" + "-" * 70)
    print("  PARTE 6: Buscando elemento inexistente")
    print("-" * 70)
    
    input("  Pressione ENTER para buscar 'XX' (não existe)...")
    tabela.buscar('XX')
    
    print("\n" + "-" * 70)
    print("  PARTE 7: Tentando inserir elemento duplicado")
    print("-" * 70)
    
    input("  Pressione ENTER para tentar inserir 'SP' novamente...")
    tabela.inserir('SP')
    
    print("\n" + "=" * 70)
    print("  RESUMO: LINEAR vs QUADRÁTICA")
    print("=" * 70)
    print("""
  ┌─────────────────────┬────────────────────┬────────────────────────┐
  │     Aspecto         │  Tentativa Linear  │  Tentativa Quadrática  │
  ├─────────────────────┼────────────────────┼────────────────────────┤
  │ Incremento          │  +1, +2, +3, ...   │  +1², +2², +3², ...    │
  │ Clustering Primário │  SIM (problema)    │  Reduzido              │
  │ Clustering Secund.  │  Não               │  Pode ocorrer          │
  │ Cache-friendly      │  SIM               │  Menos                 │
  │ Tamanho ideal       │  Qualquer          │  Número primo          │
  │ Cobertura garantida │  Todas posições    │  Depende do tamanho    │
  └─────────────────────┴────────────────────┴────────────────────────┘
    """)
    
    print("=" * 70)
    print("  FIM DA DEMONSTRAÇÃO")
    print("=" * 70)
    print(f"\n  Estado final: {tabela}")
    print()
    
    return tabela


# =============================================================================
# PONTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("        TABELA HASH - TENTATIVA QUADRÁTICA")
    print("=" * 55)
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