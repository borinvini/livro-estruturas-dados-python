# =============================================================================
# ESTRUTURA DE DADOS: PILHA (STACK) - IMPLEMENTAÇÃO COM CLASSE
# =============================================================================
# Implementação didática sem uso de métodos prontos do Python
# Métodos renomeados para evitar conflito com métodos nativos do Python
# =============================================================================


class Pilha:
    """
    Classe que implementa uma Pilha com array de tamanho fixo.
    
    Atributos:
        capacidade (int): Tamanho máximo da pilha
        dados (list): Array que armazena os elementos
        topo (int): Índice do elemento no topo (-1 se vazia)
    """
    
    def __init__(self, capacidade=5):
        self.capacidade = capacidade # tamanho do array
        self.dados = [None] * capacidade  # Array com posições vazias
        self.topo = -1  # -1 indica pilha vazia
    
    
    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.
        
        Returns:
            bool: True se vazia, False caso contrário
        """
        return self.topo == -1
    
    
    def esta_cheia(self):
        """
        Verifica se a pilha está cheia.
        
        Returns:
            bool: True se cheia, False caso contrário
        """
        return self.topo == self.capacidade - 1
    
    
    def empilhar(self, elemento):
        """
        Insere um elemento no topo da pilha (operação PUSH).
        
        Args:
            elemento: Valor a ser inserido
            
        Returns:
            bool: True se inserido com sucesso, False se pilha cheia
        """
        if self.esta_cheia():
            return False
        
        self.topo = self.topo + 1      # Incrementa o topo
        self.dados[self.topo] = elemento  # Insere na posição
        return True
    
    
    def desempilhar(self):
        """
        Remove e retorna o elemento do topo da pilha (operação POP).
        
        Returns:
            O elemento removido, ou None se a pilha estiver vazia
        """
        if self.esta_vazia():
            return None
        
        elemento = self.dados[self.topo]  # Guarda o elemento
        self.dados[self.topo] = None      # Limpa a posição
        self.topo = self.topo - 1         # Decrementa o topo
        return elemento
    
    
    def consultar_topo(self):
        """
        Retorna o elemento do topo sem removê-lo (operação PEEK/TOP).
        
        Returns:
            O elemento do topo, ou None se a pilha estiver vazia
        """
        if self.esta_vazia():
            return None
        return self.dados[self.topo]
    
    
    def tamanho(self):
        """
        Retorna a quantidade de elementos na pilha.
        
        Returns:
            int: Número de elementos armazenados
        """
        return self.topo + 1
    
    
    def exibir(self):
        """
        Exibe o conteúdo da pilha do topo até a base.
        """
        print('\n--- CONTEÚDO DA PILHA ---')
        
        if self.esta_vazia():
            print('  (pilha vazia)')
            return
        
        print('Topo → Base')
        print('-' * 15)
        
        i = self.topo
        while i >= 0:
            print(f'  [{i}] → {self.dados[i]}')
            i = i - 1
        
        print('-' * 15)
        print(f'Total de elementos: {self.tamanho()}/{self.capacidade}')


# =============================================================================
# PROGRAMA PRINCIPAL - MENU INTERATIVO
# =============================================================================

def main():
    """Função principal com menu interativo para testar a pilha."""
    
    pilha = Pilha(capacidade=5)  # Cria pilha com 5 posições
    
    print("=" * 50)
    print("ESTRUTURA DE DADOS: PILHA (STACK)")
    print("Implementação com Classe")
    print("=" * 50)
    
    while True:
        print('\n--- MENU DE OPERAÇÕES ---')
        print('1 - Inserir na pilha (PUSH)')
        print('2 - Remover da pilha (POP)')
        print('3 - Consultar topo (PEEK)')
        print('4 - Listar a pilha')
        print('5 - Sair')
        print('-' * 25)
        
        op = int(input("Escolha uma opção: "))
        
        if op == 1:  # Operação PUSH
            dado = int(input('Qual número deseja inserir? '))
            
            if pilha.empilhar(dado):
                print(f'Número {dado} inserido com sucesso!')
                print(f'Posição no topo: {pilha.topo}')
            else:
                print('Pilha cheia! Impossível inserir.')
                print(f'Capacidade máxima: {pilha.capacidade} elementos')
        
        elif op == 2:  # Operação POP
            dado_removido = pilha.desempilhar()
            
            if dado_removido is not None:
                print(f'Número {dado_removido} removido com sucesso!')
                print(f'Novo topo: {pilha.topo}')
            else:
                print('Pilha vazia! Impossível remover.')
        
        elif op == 3:  # Operação PEEK
            elemento_topo = pilha.consultar_topo()
            
            if elemento_topo is not None:
                print(f'→ Elemento no topo: {elemento_topo}')
            else:
                print('→ Pilha vazia!')
        
        elif op == 4:  # Listar pilha
            pilha.exibir()
        
        elif op == 5:  # Sair
            print('\n' + '=' * 50)
            print('Encerrando o programa...')
            print('=' * 50)
            break
        
        else:
            print('Opção inválida! Selecione uma opção de 1 a 5.')


# Executa o programa
if __name__ == "__main__":
    main()