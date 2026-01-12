class TabelaHash:
    """
    Classe que implementa uma Tabela Hash básica.
    
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
    
    def inserir(self, chave):
        """
        Insere uma chave na tabela hash.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return False
        
        posicao = self._hash_function(chave)
        
        if self.tabela[posicao] is None:
            self.tabela[posicao] = chave
            self.quantidade += 1
            print(f"\n'{chave}' inserida com sucesso na posição {posicao}!")
            return True
        else:
            print(f"\nCOLISÃO! Posição {posicao} já ocupada.'.")
            return False
    
    def remover(self, chave):
        """
        Remove uma chave da tabela hash.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return False
        
        posicao = self._hash_function(chave)
        
        if self.tabela[posicao] == chave:
            self.tabela[posicao] = None
            self.quantidade -= 1
            print(f"\n'{chave}' removida da posição {posicao}!")
            return True
        else:
            print(f"\n'{chave}' não encontrada na posição ({posicao}).")
            return False
    
    def buscar(self, chave):
        """
        Busca uma chave na tabela hash.
        """
        chave = chave.upper()
        
        if len(chave) != 2 or not chave.isalpha():
            print("\nErro: A chave deve ter exatamente 2 letras!")
            return -1
        
        posicao = self._hash_function(chave)
        
        if self.tabela[posicao] == chave:
            print(f"\n'{chave}' encontrada na posição {posicao}!")
            return posicao
        else:
            print(f"\n'{chave}' não encontrada na tabela.")
            return -1
    
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
# PONTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    main()